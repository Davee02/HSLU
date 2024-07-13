using System;
using System.Net.Sockets;

namespace PortScan; 

public class PortScan {

    public static void Main(string[] args) {
        TcpClient theClient;
        string host = "localhost";
        Console.WriteLine("Port Scanner");
        for (int port = 1; port <= 65535; port++) {
            try {
                theClient = new TcpClient(host, port);
                Console.WriteLine("Port {0} des Hosts {1} kennt TCP.", port, host);
            }
            catch (Exception e) {
                //Console.WriteLine("Port {0} des Hosts {1}: {2}", port, host, e.Message);
            }
        }
    }
}