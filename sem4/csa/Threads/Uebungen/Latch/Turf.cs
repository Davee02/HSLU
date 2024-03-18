using System;
using System.Threading;

namespace Latch;

class Turf
{

    static void Main()
    {
        ISynch startBox = new Latch();
        for (int i = 1; i <= 5; i++)
        {
            new Thread(new RaceHorse(i, startBox).Run).Start();
        }
        Console.WriteLine("Start...");
        startBox.Release();
    }
}