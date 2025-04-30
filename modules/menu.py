from modules.task import *
import json

TASK_FILE = "task.json"

def load_task():
    try:
        with open (TASK_FILE, "r") as file:
            task_data = json.load(file)
            tasklist = []
            for task in task_data:
                tasklist.append(Task.to_obj(task))
        return tasklist
    except FileNotFoundError:
        return []

def save_task(tasklist):
    with open (TASK_FILE, "w") as file:
        task_data = []
        for task in tasklist:
            task_data.append(task.to_dict())
        json.dump(task_data, file, indent=4)

tasklist = load_task()

while True:
    print("""
    Available commands:
    - add <task name>: Adds a new task.
    - mark-in-progress <id>: Marks a task as "in-progress".
    - mark-done <id>: Marks a task as "done".
    - update <id> <new description>: Updates the description of a task.
    - delete <id>: Deletes a task.
    - list: Displays all tasks.
    - list <status>: Displays tasks filtered by status (e.g., "done", "in-progress").
    - exit: Saves tasks and exits the program.
    """)
    option = input("").lower()
    option = option.split(" ")

    match option[0]:
        case "add":
            tasklist.append(Task (" ".join(option[1:])))
        
        case "mark-in-progress" | "mark-done":
            id = int(option[1])
            status = option[0][5::]
            task = Task.SearchTask(tasklist,id)
            if task != None:
                task.UpdateStatus(status)

        case "update":
            id = int (option[1])
            new = " ".join(option[2::])
            task = Task.SearchTask(tasklist, id)
            if task != None:
                task.Update(new)
        
        case "delete":
            id = int (option[1])
            new = " ".join(option[2::])
            task = Task.SearchTask(tasklist,id)
            if task != None:
                tasklist.pop(tasklist.index(task))

        case "list":
            if len(option)==1:
                Task.ListAll(tasklist)
            else:
                Task.listByStatus(tasklist,option[1])
        case "exit":
            save_task(tasklist)
            exit()
    

                    

