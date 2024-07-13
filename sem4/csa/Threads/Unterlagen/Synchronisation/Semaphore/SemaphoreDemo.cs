using System;
using System.Threading;

namespace Synchronization;

class SemaphoreDemo
{

    private static readonly Semaphore sema = new Semaphore(1, 1);

    static void Main()
    {
        for (int i = 0; i < 5; i++)
        {
            new Thread(Go).Start(i);
        }
    }
    static void Go(object number)
    {
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("{0}. Thread waits.", number);
            sema.WaitOne();
            Console.WriteLine("{0}. Thread is in critical section", number);
            Thread.Sleep(1000); // Only 3 threads can get here at once
            sema.Release();
            Console.WriteLine("{0}. Thread leaves.", number);
        }
    }
}