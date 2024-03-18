using System.Threading;

namespace NestedMonitor;

class NotifyingQueue<T>
{

    private const int SIZE = 10;
    private T[] queue = new T[SIZE];
    private int head = 0;
    private int tail = 0;
    public void Enqueue(T item)
    {
        lock (this)
        {
            head++;
            head %= SIZE;
            queue[head] = item;
            Monitor.Pulse(this);
        }
    }
    public T Dequeue()
    {
        lock (this)
        {
            if (head == tail)
            {
                Monitor.Wait(this);
            }
            tail++;
            tail %= SIZE;
            return queue[tail];
        }
    }
}