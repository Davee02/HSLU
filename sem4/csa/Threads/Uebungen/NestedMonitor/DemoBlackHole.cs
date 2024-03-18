using System;
using System.Threading;

namespace NestedMonitor;

class DemoBlackHole
{

    public static readonly BlackHole blackhole = new BlackHole();

    public static void Main()
    {
        Thread t1 = new Thread(delegate ()
        {
            Console.WriteLine(blackhole.Get().ToString());
        });
        Thread t2 = new Thread(delegate ()
        {
            blackhole.Put("Sonne, Licht, irgendetwas...");
        });
        Console.WriteLine("Wir starten die Untersuchung...");
        t1.Start();
        t2.Start();
        t1.Join();
        t2.Join();
        Console.WriteLine("Was ist passiert...");
    }
}