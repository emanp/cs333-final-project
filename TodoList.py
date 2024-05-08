from Task import Task

#For pretty display
RED = '\033[91m'
GREEN = '\033[92m'
# ANSI escape code to reset text color
RESET = '\033[0m'


class ToDoList: 
    def __init__(self): 
        self.tasks: list[Task] = [] 
        
        
    def addTask(self, task: Task):  #DONE
        if task is not None:
            self.tasks.append(task)
            print (GREEN + "Added!" + RESET)
        
        
    def editTask(self, taskIndex, newDescription): #DONE
        if taskIndex <= len(self.tasks) and taskIndex > 0:
            self.tasks[taskIndex - 1].description = newDescription 
        
        
    def deleteTask(self, taskIndex): #DONE
        if taskIndex <= len(self.tasks) and taskIndex > 0:
            del self.tasks[taskIndex - 1] 
        
        
    def markTaskAsDone(self, taskIndex): #DONE
        if taskIndex <= len(self.tasks) and taskIndex > 0:
            self.tasks[taskIndex - 1].markAsDone() 
            print (GREEN + "Marked as done." + RESET)
        
    
    def printToDoList(self): #DONE
        i = 0
        
        for task in self.tasks:
            print (GREEN + str(i+1) + ". " + task.description + RESET)
            i = i + 1