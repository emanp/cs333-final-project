
class Task
{
    private string description; 
    private bool isDone = false; 
    
    public Task(string aDescription)
    {
        description = aDescription;
    }
    
    void markAsDone()
    {
        isDone = true;
    }
    
}
