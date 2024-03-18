using System;
using System.Diagnostics;
using System.IO;

namespace ProcessSynch
{

    class Program
    {
        static void Main()
        {
            if (File.Exists("daten.txt"))
            {
                File.Delete("daten.txt");
            }
            Console.WriteLine("Press <Enter> to start...");
            Console.ReadLine();
            Process.Start("FindMinMaxNumber");
            Process.Start("AddNumbers");
            Process.Start("RandomCounter");
            Console.WriteLine("done.");
            Console.ReadLine();
        }
    }
}