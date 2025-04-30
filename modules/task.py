import time

class Task:

    id = 0
    @classmethod
    def setId(cls, tasklist):
        cls.id = tasklist[len(tasklist)-1].id
    
    def __init__(self, description):

        Task.id += 1 
        self.id = Task.id
        self.description = description
        self.status = "todo"
        self.createdAt = time.strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = time.strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
    @staticmethod
    def to_obj(dic):
        task = Task(dic["description"])
        task.id = dic["id"]
        task.status = dic["status"]
        task.createdAt = dic["createdAt"]
        task.updatedAt = dic["updatedAt"]
        return task
    
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