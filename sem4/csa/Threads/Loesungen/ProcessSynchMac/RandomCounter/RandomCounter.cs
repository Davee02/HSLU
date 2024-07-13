using System;
using System.IO;
using System.Threading;

namespace ProcessSynch {

    class RandomCounter {

        static void Main() {
            Mutex mutex = new Mutex(false, @"Global\hslu.generator");
            Random rnd = new Random();
            Console.WriteLine("Random counter");
            try {
                mutex.WaitOne();
                using (StreamWriter sw = new StreamWriter("daten.txt")) {
                    int n = 1000 + rnd.Next(5000);
                    for (int i = 0; i < n; i++) {
                        int value = -25000 + rnd.Next(50000);
                        sw.WriteLine(value);
                        Console.Write(".");
                    }
                }
            }
            finally {
                mutex.ReleaseMutex();
            }
            Console.WriteLine();
            Console.WriteLine("done.");
        }
    }
}