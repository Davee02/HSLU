using System;
using System.Threading;

namespace Synchronization;

class LockingConstruct2
{

    private static object locker = new object();

    static void Main()
    {
        long sum = 0;
        Thread t1 = new Thread(delegate ()
        {
            Monitor.Enter(locker);
            try
            {
                for (int i = 0; i <= 1_000_000; i++)
                {
                    sum += i;
                }
            }
            finally
            {
                Monitor.Exit(locker);
            }
        });
        Thread t2 = new Thread(delegate ()
        {
            Monitor.Enter(locker);
            try
            {
                Console.WriteLine("Summe = {0}", sum);
            }
            finally
            {
                Monitor.Exit(locker);
            }
        });
        t1.Start();
        t2.Start();
    }
}