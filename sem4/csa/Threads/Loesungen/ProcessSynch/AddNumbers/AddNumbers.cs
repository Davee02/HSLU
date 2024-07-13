using System;
using System.IO;
using System.Threading;

namespace ProcessSynch {

    class AddNumbers {

        static void Main() {
            Semaphore sema = new Semaphore(0, 2, "hslu.generator");
            int sum = 0;
            Console.WriteLine("Add numbers");
            try {
                sema.WaitOne();
                using (StreamReader sr = new StreamReader("daten.txt")) {
                    string line;
                    while ((line = sr.ReadLine()) != null) {
                        sum += Int32.Parse(line);
                        Console.Write("+");
                    }
                }
            }
            finally {
                sema.Release();
            }
            Console.WriteLine();
            Console.WriteLine("Sum := " + sum);
        }
    }
}