using System;
using System.Threading;

namespace Synchronization;

class LockingConstruct1
{

    private static readonly object locker = new object();

    static void Main()
    {
        long sum = 0;
        Thread t1 = new Thread(delegate ()
        {
            lock (locker)
            {
                for (int i = 0; i <= 1_000_000; i++)
                {
                    sum += i;
                }
            }
        });
        Thread t2 = new Thread(delegate ()
        {
            lock (locker)
            {
                Console.WriteLine("Summe = {0}", sum);
            }
        });
        t1.Start();
        t2.Start();
    }
}