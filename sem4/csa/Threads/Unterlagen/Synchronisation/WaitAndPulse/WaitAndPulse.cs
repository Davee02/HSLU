using System;
using System.Threading;

namespace Synchronization;

class WaitAndPulse
{

    private static readonly object synch = new object();

    static void Main()
    {
        new Thread(Waiter).Start();
        Thread.Sleep(1000);
        lock (synch)
        {
            Monitor.Pulse(synch);
        }
    }
    static void Waiter()
    {
        lock (synch)
        {
            Console.WriteLine("Waiting...");
            if (Monitor.Wait(synch, 1000))
            {
                Console.WriteLine("...Notified");
            }
            else
            {
                Console.WriteLine("Timeout");
            }
        }
    }
}