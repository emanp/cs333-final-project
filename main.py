#CS 333 - Testing & DevOps
#Author: Emanuelle Pelayo
#Date: May 7th, 2024

#example commen t
from Task import Task
from TodoList import ToDoList


def main():
    toDoList = ToDoList() 
 
    while True:
        print ("=======================================")
        print ("To-Do List")
        print ("=======================================")
        print ("1. Add Task") 
        print("2. Edit Task") 
        print("3. Delete Task") 
        print ("4. View Tasks") 
        print("5. Mark Task as Done") 
        print("0. EXIT")
        userInput = int(input("Option: "))
    
        
        if userInput == 1: #add task to the todo list 
            taskName = str(input(("Enter Task Name: ")))
            task = Task(taskName)
            toDoList.addTask(task)

        elif userInput == 2: #edit a task 
            toDoList.printToDoList()
            userChoice = int(input("Enter # of task you wish to edit: "))
            newTaskDescription = str(input("New Task Description: "))
            toDoList.editTask(userChoice, newTaskDescription)
            
        elif userInput == 3:
            toDoList.printToDoList()
            toDoList.printToDoList()
            userChoice = int(input("Enter # of task you wish to delete: "))
            toDoList.deleteTask(userChoice)
            print ("Deleted.")
            
        elif userInput == 4: #print all tasks
            toDoList.printToDoList()
            
        elif userInput == 5:
            toDoList.printToDoList()
            userChoice = int(input("Enter # of task you wish to mark as done: "))
            toDoList.markTaskAsDone(userChoice)
            
            
        elif userInput == 0:
            print ("Bye!!")
            break
                                    
if __name__ == "__main__":
    main()