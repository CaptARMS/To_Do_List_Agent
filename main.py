import random
from datetime import datetime
import LLM
        
# Task Attribute
class Task:
    def __init__(self, name, deadline, status="Not Done"):
        self.name = name
        self.deadline = datetime.strptime(deadline, '%d-%m-%Y %H:%M')
        self.status = status

    def __repr__(self):
        return f"Task(Name: {self.name}, Deadline: {self.deadline}, Status: {self.status})"


# Task manager for adding, deleting, editing, and marking tasks as done
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline):
        self.tasks.append(Task(name, deadline))

    def delete_task_with_longest_deadline(self):
        if self.tasks:
            task_to_delete = max(self.tasks, key=lambda task: task.deadline)
            self.tasks.remove(task_to_delete)
            return task_to_delete
        return None

    def edit_task(self, name, new_name=None, new_deadline=None):
        for task in self.tasks:
            if task.name == name:
                old_task = repr(task)
                if new_name:
                    task.name = new_name
                if new_deadline:
                    task.deadline = datetime.strptime(new_deadline, '%d-%m-%Y %H:%M')
                return old_task, repr(task)
        return None

    def mark_task_done(self, name):
        for task in self.tasks:
            if task.name == name:
                task.status = "Done"
                return task
        return None

    def __repr__(self):
        return "\n".join(str(task) for task in self.tasks)

#Initialize the list by adding random tasks since the initial list is not empty
def Init_manager(manager,profession,n):
    for i in range(n):
        task_name, deadline = LLM.sugg_task(profession)
        deadline = deadline.strip().strip('"')
        manager.add_task(task_name, deadline)
    return None

# Agent that randomly selects an action and logs it
def simulate_agent(manager, execution_index, log_file,profession,n=5):
    Init_manager(manager,profession,n)
    action = LLM.sugg_option(profession)
    log_entry = f"Execution {execution_index}: Task Chosen: {action}: "
    if action == "Add a new task":
        task_name, deadline = LLM.sugg_task(profession)
        deadline = deadline.strip().strip('"')
        manager.add_task(task_name, deadline)
        log_entry += f"Task Added (Name: {task_name}, Deadline: {deadline}, Status: Not Done)"
    
    elif action == "Delete an existing task":
        task_deleted = manager.delete_task_with_longest_deadline()
        if task_deleted:
            log_entry += f"Task Deleted (Name: {task_deleted.name}, Deadline: {task_deleted.deadline.date()}, Status: {task_deleted.status})"
        else:
            log_entry += "No tasks to delete"

    elif action == "Edit a task":
        if manager.tasks:
            task_to_edit = random.choice(manager.tasks).name
            new_name, new_deadline = LLM.sugg_task(profession)
            new_deadline = new_deadline.strip().strip('"')
            old_task, new_task = manager.edit_task(task_to_edit, new_name=new_name, new_deadline=new_deadline)
            log_entry += f"Task Modified from {old_task} to {new_task}"
        else:
            log_entry += "No tasks to edit"

    elif action == "Mark a task as Done":
        if manager.tasks:
            task_marked = random.choice(manager.tasks).name
            modified_task = manager.mark_task_done(task_marked)
            log_entry += f"Task Marked Done (Name: {modified_task.name}, Deadline: {modified_task.deadline}, Status: {modified_task.status})"
        else:
            log_entry += "No tasks to mark as done"


    # Write the log entry to the file
    with open(log_file, 'a') as f:
        f.write(log_entry + "\n")

    print(f"\nCurrent Tasks After Execution {execution_index}:")
    print(manager)
    print("\n")


# Example usage
task_manager = TaskManager()
log_file = "task_log.txt"
profession="barista"



# Ensure the log file is empty at the start
with open(log_file, 'w') as f:
    f.write("Task Execution Log:\n\n")

# Simulate the agent 5 times and log each action
for execution_index in range(1, 6):
    simulate_agent(task_manager, execution_index, log_file,profession)
