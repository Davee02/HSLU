using System;
using System.IO;
using System.Threading;

namespace ProcessSynch {

    class AddNumbers {

        static void Main() {
            Mutex mutex = new Mutex(false, @"Global\hslu.generator");
            int sum = 0;
            Console.WriteLine("Add numbers");
            try {
                mutex.WaitOne();
                using (StreamReader sr = new StreamReader("daten.txt")) {
                    string line;
                    while ((line = sr.ReadLine()) != null) {
                        sum += Int32.Parse(line);
                        Console.Write("+");
                    }
                }
            }
            finally {
                mutex.ReleaseMutex();
            }
            Console.WriteLine();
            Console.WriteLine("Sum := " + sum);
        }
    }
}