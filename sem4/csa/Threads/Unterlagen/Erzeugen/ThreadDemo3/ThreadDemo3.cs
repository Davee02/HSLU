using System;
using System.Threading;

namespace ThreadDemos;

class ThreadDemo3
{

    private bool done = false;

    static void Main()
    {
        ThreadDemo3 tt = new ThreadDemo3();
        new Thread(tt.Go).Start();
        tt.Go();
    }
    void Go()
    {
        if (!done)
        {
            //Thread.Yield();
            done = true;
            Console.WriteLine("Done");
        }
    }
}