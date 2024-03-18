using System;
using System.IO;
using System.Threading;

namespace ProcessSynch;

class FindMinMaxNumber
{

    static void Main()
    {
        int min = 0;
        int max = 0;
        Console.WriteLine("Find min./max. number");
        using (StreamReader sr = new StreamReader("daten.txt"))
        {
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                int num = Int32.Parse(line);
                min = min > num ? num : min;
                max = max < num ? num : max;
                Console.Write("*");
            }
        }
        Console.WriteLine();
        Console.WriteLine("Min := {0}", min);
        Console.WriteLine("Max := {0}", max);
    }
}