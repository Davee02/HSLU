using System;
using System.Threading;

namespace Synchronization;

class SimpleBlocking
{

    static void Main()
    {
        long sum = 0;
        bool fertig = false;
        Thread summieren = new Thread(delegate ()
        {
            for (int i = 0; i <= 1_000_000_000; i++)
            {
                sum += i;
            }
            fertig = true;
        });
        summieren.Start();
        // Variante 1
        //while (!fertig) ;
        // Variante 2
        //Thread.Sleep(10000);
        // Variante 3
        summieren.Join();
        Console.WriteLine("Summe = {0}", sum);
    }
}