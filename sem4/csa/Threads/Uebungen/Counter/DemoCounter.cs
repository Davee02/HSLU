using System;
using System.Threading;

namespace Counter;

class DemoCounter
{

    private readonly string id;
    private readonly Counter counter;

    public DemoCounter(string id, Counter counter)
    {
        this.id = id;
        this.counter = counter;
    }
    void Go()
    {
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(id + counter.NextNumber());
            Thread.Sleep(50);
        }
    }
    static void Main()
    {
        Counter counter = new Counter();
        DemoCounter ct1 = new DemoCounter("T1: ", counter);
        DemoCounter ct2 = new DemoCounter("T2: ", counter);
        DemoCounter ct3 = new DemoCounter("T3: ", counter);
        new Thread(ct1.Go).Start();
        new Thread(ct2.Go).Start();
        new Thread(ct3.Go).Start();
    }
}