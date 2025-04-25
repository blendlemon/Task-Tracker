import time

class Task:

    id = 0
    
    def __init__(self, description):

        Task.id += 1 
        self.id = Task.id
        self.description = description
        self.status = "todo"
        self.createdAt = time.strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = time.strftime("%Y-%m-%d %H:%M:%S")
    
    def Update(self, description):
        self.description = description
        self.UpdateTime()

    def UpdateTime(self):
        self.updatedAt = time.strftime("%Y-%m-%d %H-%M-%S")

    def UpdateStatus(self, status):
        self.status = status
        self.UpdateTime()

    @staticmethod
    def SearchTask(tasklist, id):
        for task in tasklist:
            if task.id == id:
                return task
    
    @staticmethod
    def ListAll(tasklist):
        for task in tasklist:
            print(vars(task))
    
    @staticmethod
    def listByStatus(tasklist, status):
        for task in tasklist:
            if task.status == status:
                print(vars(task))
                