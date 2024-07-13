using System;
using System.Net.Sockets;

namespace PortScanSema {

    public class Handler {

        private readonly string host;
        private readonly int port;

        public Handler(string host, int port) {
            this.host = host;
            this.port = port;
        }

        public void Do() {
            try {
                TcpClient theClient = new TcpClient(host, port);
                Console.WriteLine("Port {0} des Hosts {1} kennt TCP.", port, host);
            }
            catch (Exception) {
                if ((port + 1) % 5000 == 0)
                    Console.WriteLine("{0} Ports untersucht", port + 1);
            }
        }
    }
}