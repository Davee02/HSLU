using System;

namespace NestedMonitor;

class BlackHole
{

    private readonly NotifyingQueue<string> queue = new();

    public void Put(string thing)
    {
        lock (this)
        {
            queue.Enqueue(thing);
        }
    }
    public String Get()
    {
        lock (this)
        {
            return queue.Dequeue();
        }
    }
}