using System;
using System.Threading;

namespace ThreadDemos;

class ThreadDemo6
{

    static void Main()
    {
        Thread t = new Thread(Go);
        t.Start(true);
        Go(false);
    }
    static void Go(object upperCase)
    {
        bool upper = (bool)upperCase;
        Console.WriteLine(upper ? "HELLO!" : "hello!");
    }
}