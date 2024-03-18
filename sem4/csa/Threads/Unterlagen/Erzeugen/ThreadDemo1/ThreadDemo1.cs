using System;
using System.Threading;

namespace ThreadDemos;

class ThreadDemo1
{

    static void Main()
    {
        Thread t = new Thread(WriteY);
        t.Start();
        for (int i = 0; i < 1000; i++) Console.Write("x");
    }
    static void WriteY()
    {
        for (int i = 0; i < 1000; i++) Console.Write("y");
    }
}