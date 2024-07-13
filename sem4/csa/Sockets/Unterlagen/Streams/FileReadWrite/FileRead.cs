using System;
using System.IO;

namespace FileReadWrite; 
class FileRead {
    public static void DoIt() {
        try {
            using (StreamReader sr =
                new StreamReader("daten.txt",System.Text.Encoding.UTF8)) {
                string line;
                while ((line = sr.ReadLine()) != null) {
                    Console.WriteLine(line);
                }
            }
            Console.WriteLine("Datei gelesen.");
        }
        catch (Exception e) {
            Console.WriteLine(e.ToString());
        }
    }
}