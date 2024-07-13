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
            Process.Start(new ProcessStartInfo() {
                FileName = "dotnet",
                Arguments = "RandomCounter.dll",
            });
            Thread.Sleep(100);
            Process.Start(new ProcessStartInfo() {
                FileName = "dotnet",
                Arguments = "FindMinMaxNumber.dll",
            });
            Process.Start(new ProcessStartInfo() {
                FileName = "dotnet",
                Arguments = "AddNumbers.dll",
            });
        }
    }
}