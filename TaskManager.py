# TaskManager.py
from Project import Project

class TaskManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def display_projects(self):
        print("Projects in the Task Manager:")
        for project in self.projects:
            project.display_info()
            print()
