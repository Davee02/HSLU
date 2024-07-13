using System;
using System.Threading;

namespace PortScanSema {

    public class PortScan {
        private static readonly string host = "localhost";
        private static int nThreads = 10_000;
        private static Semaphore sema;

        public static void Main(string[] args) {
            if (args.Length != 0) {
                try {
                    nThreads = Int32.Parse(args[0]);
                }
                catch (FormatException e) {
                    Console.WriteLine(e.Message);
                }
            }
            sema = new Semaphore(nThreads, nThreads);
            Console.WriteLine("Port Scanner...");
            for (int port = 1; port <= 65535; port++) {
                sema.WaitOne();
                new Thread(DoScan).Start(port);
            }
        }
        private static void DoScan(Object obj) {
            int port = (Int32)obj;
            new Handler(host, port).Do();
            sema.Release();
        }
    }
}