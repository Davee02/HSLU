using System;
using System.IO;
using System.Threading;

namespace ProcessSynch {

    class RandomCounter {

        static void Main() {
            Semaphore sema = new Semaphore(0, 2, "hslu.generator");
            Random rnd = new Random();
            Console.WriteLine("Random counter");
            try {
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
                sema.Release(2);
            }
            Console.WriteLine();
            Console.WriteLine("done.");
        }
    }
}