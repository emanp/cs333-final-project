#Unit tests for Task.py
import unittest

from Task import Task 

class Test_Task(unittest.TestCase):
    #unit test 
    def test_markAsDone(self):
        task = Task("Study")
        self.assertFalse(task.isDone)
        task.markAsDone()
        self.assertTrue(task.isDone)
        self.assertIsNotNone(task.isDone)
    
    #unit test
    def test_init(self):
        task = Task ("Study")
        self.assertFalse(task.isDone)
        self.assertIs(type(task.description), str)
        
if __name__ == "__main__":
    unittest.main()
        
        
        