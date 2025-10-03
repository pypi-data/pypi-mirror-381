"""
    Top level library defs
"""

from .project import DatastarProject
from .macro import DatastarMacro
from .task import DatastarTask


def create_project(project_name: str) -> DatastarProject:
    """
    Create a new Datastar project

    Args:
    project_name: The name of the new project to be created

    Returns: DatastarProject instance, or None if already exists
    """
    print("create_project in init")
    return DatastarProject(project_name, True)


def connect_project(project_name: str) -> DatastarProject:
    """
    Connect to an existing Datastar project

    Args:
    project_name: The name of the new project to be created

    Returns: DatastarProject instance, or None if already exists
    """
    print("create_project in init")
    return DatastarProject(project_name, False)
