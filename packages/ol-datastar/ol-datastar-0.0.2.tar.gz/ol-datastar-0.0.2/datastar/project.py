from .macro import DatastarMacro
from typing import Dict


class DatastarProject:

    def create(self):
        """
        Create a new Datastar project

        Args:
        project_name: The name of the new project to be created

        Returns: DatastarProject instance, or None if already exists
        """

        print(f"Creating new datastar project: {self.project_name}")

    def connect_to(self):
        """
        Connect to an existing Datastar project

        Args:
        project_name: The name of the existing project to be connected to

        Returns: DatastarProject instance, or None if does not exist
        """
        print(f"Connecting to existing datastar project: {self.project_name}")

    def __init__(self, project_name: str, exists: bool):

        self.project_name = project_name
        self.macros: Dict[str, DatastarMacro] = {}

        if not exists:
            self.create()
        else:
            self.connect_to()

    def add_macro(self, macro_name: str) -> DatastarMacro:
        """
        Create a new macro within this project

        Args:
        macro_name: The name of the new macro to be created

        Returns: DatastarProject instance, or None if already exists
        """
        print(f"Created macro {macro_name}")
        new_macro = DatastarMacro(macro_name)
        self.macros[macro_name] = new_macro
        return new_macro

    def get_macro(self, macro_name: str) -> DatastarMacro | None:
        """
        Get an existing macro within this project

        Args:
        macro_name: The name of the macro to be returned

        Returns: DatastarProject instance, or None if already exists
        """

        return self.macros.get(macro_name)

    def get_all_macros(self) -> dict[str, DatastarMacro]:
        """
        Return all macros within this project
        """

        return self.macros
