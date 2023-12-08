# Main.py
from Task import Task
from Project import Project
from TaskManager import TaskManager

# Create tasks
task1 = Task(1, "Implement feature A", "High")
task2 = Task(2, "Fix bug in module B", "Medium")

# Create projects
project1 = Project(101, "Project X")
project2 = Project(102, "Project Y")

# Add tasks to projects
project1.add_task(task1)
project2.add_task(task2)

# Create Task Manager and add projects
task_manager = TaskManager()
task_manager.add_project(project1)
task_manager.add_project(project2)

# Display project information
task_manager.display_projects()
