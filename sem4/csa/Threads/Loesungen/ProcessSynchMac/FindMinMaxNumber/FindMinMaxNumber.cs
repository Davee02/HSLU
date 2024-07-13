using System;
using System.IO;
using System.Threading;

namespace ProcessSynch {

    class FindMinMaxNumber {

        static void Main() {
            Mutex mutex = new Mutex(false, @"hslu.generator");
            int min = 0;
            int max = 0;
            Console.WriteLine("Find min./max. number");
            try {
                mutex.WaitOne();
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
                mutex.ReleaseMutex();
            }
            Console.WriteLine();
            Console.WriteLine("Min := " + min);
            Console.WriteLine("Max := " + max);
        }
    }
}