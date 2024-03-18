using System;
using System.Threading;

namespace LostSignals;

class Operator
{

    public const int MAXCOUNT = 4;
    private int counter = 0;
    private readonly ISynch signal;
    private readonly Random rnd;
    private readonly EventWaitHandle next = new AutoResetEvent(false);

    public Operator(ISynch signal)
    {
        this.signal = signal;
        rnd = new Random();
    }
    private void Init()
    {
        lock (this)
        {
            counter = MAXCOUNT;
            Console.WriteLine("Es wurden {0} Operationen vorbereitet...", counter);
        }
    }
    public int Operation()
    {
        lock (this)
        {
            return rnd.Next(1000);
        }
    }
    public void Done(string id)
    {
        lock (this)
        {
            counter++;
            Console.WriteLine("{0}. Operation wurde durch {1} beendet.", counter, id);
            if (counter == MAXCOUNT)
            {
                next.Set();
            }
        }
    }
    public void Do()
    {
        while (true)
        {
            this.Init();
            lock (this)
            {
                for (; counter > 0; counter--)
                {
                    signal.Release();
                }
            }
            next.WaitOne();
        }
    }
}