using System;
using System.IO;
using System.Threading;

namespace ProcessSynch {

    class FindMinMaxNumber {

        static void Main() {
            Semaphore sema = new Semaphore(0, 2, "hslu.generator");
            int min = 0;
            int max = 0;
            Console.WriteLine("Find min./max. number");
            try {
                sema.WaitOne();
                using (StreamReader sr = new StreamReader("daten.txt")) {
                    string line;
                    while ((line = sr.ReadLine()) != null) {
                        int num = Int32.Parse(line);
                        min = min > num ? num : min;
                        max = max < num ? num : max;
                        Console.Write("*");
                    }
                }
            }
            finally {
                sema.Release();
            }
            Console.WriteLine();
            Console.WriteLine("Min := " + min);
            Console.WriteLine("Max := " + max);
        }
    }
}