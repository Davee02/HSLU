using System;
using System.Threading;

namespace PortScan {

    public class PortScan {

        public static void Main() {
            string host = "localhost";
            Console.WriteLine("Initialisierung...");
            Console.WriteLine("Port Scanner");
            for (int port = 1; port <= 65535; port++) {
                new Thread(new Handler(host, port).Do).Start();
            }
        }
    }
}
