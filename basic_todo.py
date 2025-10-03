class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.markcompleted = False
    def mark_completed(self):
        self.markcompleted = True
    def __str__(self):
        status = None
        if self.markcompleted == True:
            return "Done"
        else:
            return "First Complete it"
t = "OOPs"
d = "Have to learn OOPs"
my_task = Task(t,d)
my_task.mark_completed()
print(my_task)