from typing import Any, Callable, Dict, Self

from .. import OpenMaya2, cmds
from ..log import get_logger
from ..nodes import cast

logger = get_logger(__name__)
logger.setLevel("DEBUG")


class Node:
    _cmds_creator: Callable[..., str]
    _cmds_creator_args: Dict[str, Any] = {}

    def __init__(self, node_path: str):
        self.node_path = node_path

    def __str__(self):
        return self.node_path

    def __repr__(self):
        return f'{type(self).__name__}("{str(self)}")'

    def rename(self, new_name: str, *args, **kwargs) -> str:
        """
        Rename the current node. If new name is not unique maya will resolve a new unique name.
        :param new_name: The new name of the node.
        :return: The new name of the node.
        """
        actual_new_name = cmds.rename(str(self), new_name, *args, **kwargs)
        self.node_path = actual_new_name
        return actual_new_name

    def _cmd_caller(self, func_name, *args, **kwargs):
        return cmds.attr(func_name, self.node_path, *args, **kwargs)

    @classmethod
    def create(cls, name: str, **kwargs) -> Self:
        """
        Create a new transform node.
        :param name: The name of the new transform node.
        :return: The new transform node.
        """
        kwargs.update(cls._cmds_creator_args)
        kwargs["name"] = name
        cmds_value = cls._cmds_creator(**kwargs)  # noqa: E1102
        if cmds_value != name:
            logger.debug(f"Name was not unique. New name: {cmds_value}.")
        return cls(cmds_value)


class DagNode(Node):
    def __init__(self, node_path: str):
        super().__init__(node_path)
        self.dag_path = cast.get_dag_path_from_string(node_path)

    def __str__(self):
        return self.get_full_path()

    def get_depend_node(self) -> OpenMaya2.MObject:
        """
        Get the depend node of the current node.
        :return: The depend node of the current node.
        """
        return self.dag_path.node()

    def get_full_path(self) -> str:
        """
        Get the full path of the current node.
        :return: The full path of the current node.
        """
        full_path = self.dag_path.fullPathName()
        if not full_path:
            logger.warning(f"Node has been deleted. Original path: {self.node_path}")
        return full_path

    def get_mfndependency_node(self) -> OpenMaya2.MFnDependencyNode:
        """
        Get the MFnDependencyNode of the current node.
        :return: The MFnDependencyNode of the current node.
        """
        return OpenMaya2.MFnDependencyNode(self.get_depend_node())


class Transform(DagNode):
    _cmds_creator = cmds.group
    _cmds_creator_args = {"empty": True}
