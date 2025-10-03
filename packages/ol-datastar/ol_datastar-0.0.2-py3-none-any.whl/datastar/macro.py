from .task import DatastarTask
from typing import Dict


class DatastarMacro:

    def __init__(self, macro_name: str):
        self.macro_name = macro_name

        self.tasks: Dict[str, DatastarTask] = {}

    def add_input_task(self, task_name: str) -> DatastarTask:

        # TODO: Connection logic (Connect to last, nearest, specified etc.)
        # TODO: Consider positioning on UI canvas (in case created programatic and later edited via UI)
        # TODO: 
        
        print(f"Created task {task_name}")
        new_task = DatastarTask(task_name)
        self.tasks[task_name] = new_task
        return new_task

    def get_all_tasks(self) -> Dict[str, DatastarTask]:
        """
        Return tasks within this macro
        """

        return self.tasks
