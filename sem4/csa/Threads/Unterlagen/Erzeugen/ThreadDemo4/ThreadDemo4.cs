using System;
using System.Threading;

namespace ThreadDemos;

class ThreadDemo4
{

    static void Main()
    {
        Thread t = new Thread(new ThreadStart(Go));
        t.Start();
        Go();
    }
    static void Go()
    {
        Console.WriteLine("hello!");
    }
}