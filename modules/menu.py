from modules.task import *

tasklist = []
while True:
    option = input("").lower()
    option = option.split()

    match option[0]:
        case "add":
            tasklist.append(Task (" ".join(option[1:])))
        
        case "mark-in-progress", "mark-done":
            print("hla")
            id = int(option[1])
            status = option[0][3::]
            print(status)
            Task.SearchTask(tasklist,id).UpdateStatus(status)

        case "list":
            if len(option)==1:
                Task.ListAll(tasklist)
            else:
                Task.listByStatus(tasklist,option[1])
                    

