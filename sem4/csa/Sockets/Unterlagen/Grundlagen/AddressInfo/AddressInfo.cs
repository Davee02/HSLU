using System;
using System.Net;
using System.Net.Sockets;
using System.IO;

namespace AddressInfo {
    public class AddressInfo {
        static void Main() {
            DoGetHostEntry("localhost");
            DoGetHostEntry(Environment.MachineName);
        }

        public static void DoGetHostEntry(string hostname) {
            IPHostEntry host = Dns.GetHostEntry(hostname);
            Console.WriteLine("GetHostEntry({0}) returns:", hostname);
            Console.WriteLine("Host name : " + host.HostName);
            for (int i = 0; i < host.AddressList.Length; i++) {
                Console.WriteLine("AddressList[{0}]: {1}", i, host.AddressList[i]);
            }
            Console.WriteLine();
        }
    }
}
