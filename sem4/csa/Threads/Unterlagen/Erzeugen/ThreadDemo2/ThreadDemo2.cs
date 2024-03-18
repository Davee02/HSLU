using System;
using System.Threading;

namespace ThreadDemos;

class ThreadDemo2
{

    static void Main()
    {
        new Thread(Go).Start();
        ThreadDemo2.Go();
    }
    static void Go()
    {
        for (int i = 0; i < 10; i++)
        {
            Console.Write('x');
        }
    }
}