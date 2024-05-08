class Task: 
    def __init__(self, description: str): 
        self.description = description 
        self.isDone = False 
        
    def markAsDone(self): 
        self.isDone = True
    
    