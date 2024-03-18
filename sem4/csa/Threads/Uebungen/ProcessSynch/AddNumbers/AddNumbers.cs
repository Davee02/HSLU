using System;
using System.IO;
using System.Threading;

namespace ProcessSynch;

class AddNumbers
{

    static void Main()
    {
        int sum = 0;
        Console.WriteLine("Add numbers");
        using (StreamReader sr = new StreamReader("daten.txt"))
        {
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                sum += Int32.Parse(line);
                Console.Write("+");
            }
        }
        Console.WriteLine();
        Console.WriteLine("Summe := {0}", sum);
    }
}