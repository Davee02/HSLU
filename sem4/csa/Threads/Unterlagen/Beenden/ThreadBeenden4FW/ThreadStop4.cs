using System;
using System.Threading;

namespace ThreadBeenden
{

    class ThreadStop4
    {

        static void Main()
        {
            Thread t = new Thread(Work);
            t.Start();
            Thread.Sleep(1000); t.Abort();
            Thread.Sleep(1000); t.Abort();
            Thread.Sleep(1000); t.Abort();
        }
        static void Work()
        {
            while (true)
            {
                try
                {
                    while (true) ; // Endlosschleife
                }
                catch (ThreadAbortException)
                {
                    Thread.ResetAbort();
                }
                Console.WriteLine("I will not die!");
            }
        }
    }
}