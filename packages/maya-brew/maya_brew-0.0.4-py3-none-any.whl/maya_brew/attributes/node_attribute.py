import typing

from .. import OpenMaya2, cmds
from ..nodes import cast
from ..nodes.node_types import DagNode, Node

PlugInput = typing.Union[OpenMaya2.MPlug, str]
A = typing.TypeVar("A", bound="Attribute")


class Attribute:
    _getter_type: str

    def __new__(cls: type[A], plug_or_path: PlugInput) -> A:
        if cls is not Attribute:
            return typing.cast(A, super().__new__(cls))

        if isinstance(plug_or_path, OpenMaya2.MPlug):
            plug = plug_or_path
        elif isinstance(plug_or_path, str):
            plug = cls._plug_from_path(plug_or_path)
        else:
            raise ValueError("plug_or_path must be an MPlug or attribute path string.")

        try:
            mobj_attr = plug.attribute()
        except (RuntimeError, ValueError) as e:
            raise RuntimeError(
                f"Failed to obtain MObject attribute for plug {plug}"
            ) from e

        api_type = getattr(mobj_attr, "apiTypeStr", None)
        if not api_type:
            raise RuntimeError(
                f"Attribute object for plug {plug} has no apiTypeStr; cannot dispatch."
            )

        try:
            subclass: type[Attribute] = _API_TYPE_SUBCLASS_MAP[api_type]
        except KeyError:
            raise NotImplementedError(
                f"Unsupported attribute apiTypeStr '{api_type}'. "
                f"Known types: {sorted(_API_TYPE_SUBCLASS_MAP)}"
            )

        instance = super().__new__(subclass)
        setattr(instance, "_pre_init_plug", plug)
        return typing.cast(A, instance)

    @typing.overload
    def __init__(self, plug_or_path: str): ...

    @typing.overload
    def __init__(self, plug_or_path: OpenMaya2.MPlug): ...

    def __init__(self, plug_or_path: PlugInput):
        # _pre_init_plug is injected by Attribute.__new__ ONLY when the user called
        # Attribute(...) (base class factory dispatch). Direct subclass construction
        # (e.g. FloatAttribute(...)) bypasses that path, so pre will be None and we
        # must resolve plug_or_path here.
        pre = getattr(self, "_pre_init_plug", None)
        if pre is not None:
            self.plug = pre
            delattr(self, "_pre_init_plug")
            return

        if isinstance(plug_or_path, OpenMaya2.MPlug):
            self.plug = plug_or_path
        elif isinstance(plug_or_path, str):
            self.plug = self._plug_from_path(plug_or_path)
        else:
            raise ValueError("plug_or_path must be an MPlug or attribute path string.")

    @staticmethod
    def _plug_from_path(path: str) -> OpenMaya2.MPlug:
        """
        Resolve a string path to an MPlug.
        :param path: The full path to the attribute, e.g. '|grp|node|nodeShape.visibility'
        :return: The MPlug for the attribute.
        """
        # Split path into node path and attribute name
        if "." not in path:
            raise ValueError(
                "Attribute path must include a '.' separating node and attribute."
            )
        node_path, attr_name = path.rsplit(".", 1)
        node_dag_path = cast.get_dag_path_from_string(node_path)
        node = DagNode(node_dag_path.fullPathName())
        plug = Attribute._get_plug_from_node(node, attr_name)
        return plug

    def __str__(self):
        return self.name()

    def get(self):
        return self._get_plug_value(self.plug)

    def set(self, value):
        attr_name = self.plug.name()
        cmds.setAttr(attr_name, value)

    def node(self):
        return self._get_node_from_plug(self.plug)

    def name(self):
        raise NotImplementedError

    def connect(self, dest: "Attribute", force: bool = False, next_available=False):
        """
        Connect this attribute to another attribute.
        :param dest: The destination attribute to connect to.
        :param force: Whether to force the connection if the destination is already connected.
        :param next_available: Whether to connect to the next available index if the destination is an array attribute.
        """
        cmds.connectAttr(
            self.plug.name(),
            dest.plug.name(),
            force=force,
            nextAvailable=next_available,
        )

    def disconnect(self, dest: "Attribute", next_available=False):
        """
        Disconnect this attribute from another attribute.
        :param dest: The destination attribute to disconnect from.
        :param next_available: Whether to disconnect from the next available index if the destination is an
        array attribute.
        """
        cmds.disconnectAttr(
            self.plug.name(), dest.plug.name(), nextAvailable=next_available
        )

    @classmethod
    def _get_value(cls, node: DagNode, attr_name: str):
        plug = cls._get_plug_from_node(node, attr_name)
        return cls._get_plug_value(plug)

    @staticmethod
    def _get_plug_from_node(node: DagNode, attr_name: str) -> OpenMaya2.MPlug:
        fn_dep = node.get_mfndependency_node()
        return fn_dep.findPlug(attr_name, False)

    @staticmethod
    def _get_node_from_plug(plug: OpenMaya2.MPlug) -> Node:
        mobj = plug.node()
        if mobj.hasFn(OpenMaya2.MFn.kDagNode):
            return DagNode(OpenMaya2.MFnDagNode(mobj).fullPathName())
        else:
            name = OpenMaya2.MFnDependencyNode(mobj).name()
            return Node(name)

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        return getattr(plug, cls._getter_type)()


class FloatAttribute(Attribute):
    _getter_type = "asDouble"


class MessageAttribute(Attribute):
    _getter_type = "kMessage"

    @classmethod
    def _get_plug_value(cls, plug: OpenMaya2.MPlug):
        raise AttributeError("Message attributes do not hold data.")

    @classmethod
    def set(cls, value):
        raise AttributeError("Message attributes are not settable.")


_API_TYPE_SUBCLASS_MAP = {
    "kDoubleLinearAttribute": FloatAttribute,
    "kMessageAttribute": MessageAttribute,
}
