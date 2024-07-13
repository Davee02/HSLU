using System;
using System.IO;

namespace FileReadWrite; 
class FileWrite {
    public static void DoIt() {
        try {
            using (StreamWriter sw =
                new StreamWriter("daten.txt",false,System.Text.Encoding.UTF8)) {
                string[] text = { "Titel", "Köln", "4711" };
                for (int i = 0; i < text.Length; i++)
                    sw.WriteLine(text[i]);
            }
            Console.WriteLine("Datei geschrieben.");
        }
        catch (Exception e) {
            Console.WriteLine(e);
        }
    }
}