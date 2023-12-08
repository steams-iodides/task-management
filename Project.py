# Project.py
from Task import Task

class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_info(self):
        print(f"Project ID: {self.project_id}")
        print(f"Project Name: {self.name}")
        print("\nTasks in the Project:")
        for task in self.tasks:
            task.display_info()
            print()
