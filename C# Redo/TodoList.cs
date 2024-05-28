
using System; 
using System.Collections.Generic;

class TodoList
{
    private List<Task> todoList;
    TodoList()
    {
        todoList = new List<Task>();
    }
    
    
    void addTask(Task task)
    {
        if (task != null)
        {
            todoList.Add(task);
            Console.WriteLine("Added!");
        }
    }
}
    
