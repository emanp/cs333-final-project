#unit and integration tests for TodoList.py

from TodoList import ToDoList
from Task import Task 

import unittest 

class Test_TodoList(unittest.TestCase):
    
    #integration, unittest
    def test_addTask(self):
        task = Task("Clean")
        task1 = Task ("Procastinate")
        toDoList = ToDoList()
        toDoList.addTask(task)
        toDoList.addTask(task1)
        
        self.assertEqual(toDoList.tasks[0].description, "Clean")
        self.assertEqual(toDoList.tasks[1].description, "Procastinate")
        self.assertNotEqual(toDoList.tasks[0], None)
        self.assertNotEqual(toDoList.tasks[0], None)
        
        taskToFail = Task(None)
        self.assertEqual(len(toDoList.tasks), 2)
        
    #integration, unit test    
    def test_editTask(self):
        task = Task("Clean")
        toDoList = ToDoList()
        toDoList.addTask(task)
        
        toDoList.editTask(0, "Do Homework")
        self.assertEqual(task.description, "Do Homework")
        toDoList.editTask(1, "Clean")
        self.assertNotEqual(task.description, "Clean") #should stay as "Do Homework"
    
    #integration, unit test 
    def test_deleteTask_within_range(self):
        task = Task("Clean")
        task1 = Task ("Procastinate")
        toDoList = ToDoList()
        toDoList.addTask(task)
        toDoList.addTask(task1)
        
        toDoList.deleteTask(1)
        self.assertEqual(toDoList.tasks[0].description, "Procastinate")
    
    #integration, unit test 
    def test_deleteTask_out_of_range(self):
        task = Task("Clean")
        task1 = Task ("Procastinate")
        toDoList = ToDoList()
        toDoList.addTask(task)
        toDoList.addTask(task1)
        
        #less than lowest index
        toDoList.deleteTask(0)
        self.assertEqual(len(toDoList.tasks), 2) #unchanged size
        
        #greater than highest index
        toDoList.deleteTask(3)
        self.assertEqual(len(toDoList.tasks), 2) #unchanged size
        
    #integration, unit test 
    def test_markTaskAsDone_within_range(self):
        task = Task("Clean")
        task1 = Task ("Procastinate")
        toDoList = ToDoList()
        toDoList.addTask(task)
        toDoList.addTask(task1)
        
        toDoList.markTaskAsDone(1)
        self.assertTrue(task.isDone) 
        
        toDoList.markTaskAsDone(2)
        self.assertTrue(task.isDone) 
        
    #integration, unit test    
    def test_markTaskAsDone_out_of_bounds(self):
        task = Task("Clean")
        task1 = Task ("Procastinate")
        toDoList = ToDoList()
        toDoList.addTask(task)
        toDoList.addTask(task1)
        
        #less than lowest index
        toDoList.markTaskAsDone(0)
        self.assertFalse(task.isDone) 
        
        #higher than highest index
        toDoList.markTaskAsDone(3)
        self.assertFalse(task.isDone) 
        
if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
    
        
    
        
    
        
        
        