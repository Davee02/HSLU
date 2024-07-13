using System;
using System.Threading;

namespace Synchronization;

class BasicWaitHandle
{

    private static readonly EventWaitHandle wh = new ManualResetEvent(false);

    static void Main()
    {
        var t1 = new Thread(Waiter);
        var t2 = new Thread(Waiter);
        t1.Start();
        t2.Start();
        Thread.Sleep(1000);
        wh.Set();
        //wh.Set();
    }
    static void Waiter()
    {
        Console.WriteLine("Waiting...");
        wh.WaitOne();
        Console.WriteLine("...Notified");
    }
}