# Task.py
class Task:
    def __init__(self, task_id, description, priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority

    def display_info(self):
        print(f"Task ID: {self.task_id}")
        print(f"Description: {self.description}")
        print(f"Priority: {self.priority}")
