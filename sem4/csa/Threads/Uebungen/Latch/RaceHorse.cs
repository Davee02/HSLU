using System;
using System.Threading;

namespace Latch;

class RaceHorse
{

    private readonly ISynch startSignal;
    private readonly int nr;

    public RaceHorse(int nr, ISynch startSignal)
    {
        this.nr = nr;
        this.startSignal = startSignal;
    }
    public void Run()
    {
        Console.WriteLine("Rennpferd {0} geht in die Startbox.", nr);
        startSignal.Acquire();
        Console.WriteLine("Rennpferd {0} l�uft los.", nr);
        Thread.Sleep(new Random().Next(3000));
        Console.WriteLine("Rennpferd {0} ist im Ziel.", nr);
    }
}