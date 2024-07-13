using System;
using System.Diagnostics;
using System.IO;
using System.Threading;

namespace ProcessSynch {
    class Program {
        static void Main() {
            if (File.Exists("daten.txt")) {
                File.Delete("daten.txt");
            }
            Console.WriteLine("Press <Enter> to start...");
            Console.ReadLine();
            Process.Start("RandomCounter");
            Thread.Sleep(500);
            Process.Start("FindMinMaxNumber");
            Process.Start("AddNumbers");
            Console.WriteLine("done.");
            Console.ReadLine();
        }
    }
}