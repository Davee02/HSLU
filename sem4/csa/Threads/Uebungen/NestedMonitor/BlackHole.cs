using System;

namespace NestedMonitor;

class BlackHole
{

    private readonly NotifyingQueue<string> queue = new();

    public void Put(string thing)
    {

            queue.Enqueue(thing);
        
    }
    public String Get()
    {
        
            return queue.Dequeue();
        
    }
}