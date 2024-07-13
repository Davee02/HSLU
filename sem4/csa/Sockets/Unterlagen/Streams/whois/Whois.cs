using System;
using System.Net.Sockets;
using System.IO;

namespace TcpReadWrite {
    class Whois {
        public static void Main() {
            using (TcpClient client = new TcpClient("whois.nic.ch", 43)) { 
                StreamWriter outStream = new StreamWriter(client.GetStream());
                StreamReader inStream = new StreamReader(client.GetStream());
                outStream.WriteLine("hslu.ch");
                outStream.Flush();
                string line;
                while ((line = inStream.ReadLine()) != null) {
                    Console.WriteLine(line);
                }
            }
        }
    }
}
