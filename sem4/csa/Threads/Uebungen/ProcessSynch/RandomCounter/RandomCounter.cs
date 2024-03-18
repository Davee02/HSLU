using System;
using System.IO;
using System.Threading;

namespace ProcessSynch;

class RandomCounter
{

    static void Main()
    {
        Random rnd = new Random();
        Console.WriteLine("Random counter");
        using (StreamWriter sw = new StreamWriter("daten.txt"))
        {
            int n = 1000 + rnd.Next(5000);
            for (int i = 0; i < n; i++)
            {
                int value = -25_000 + rnd.Next(50_000);
                sw.WriteLine(value);
                Console.Write(".");
            }
        }
        Console.WriteLine();
        Console.WriteLine("done.");
    }
}
