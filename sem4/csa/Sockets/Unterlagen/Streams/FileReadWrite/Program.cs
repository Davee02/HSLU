using System;
using System.IO;

namespace FileReadWrite {
    class Program {
        static void Main() {
            if (File.Exists("daten.txt")) {
                File.Delete("daten.txt");
            }
            Console.WriteLine("<Enter> zum Start drücken...");
            Console.ReadLine();
            FileWrite.DoIt();
            FileRead.DoIt();
        }
    }
}