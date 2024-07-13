using System;
using System.Net;
using System.Net.Sockets;
using System.IO;

namespace IterativerServer; 
public class IterativerServer {
    public static void Main() {
        TcpListener listen = new TcpListener(IPAddress.Any, 7070);
        listen.Start();
        while (true) {
            Console.WriteLine("Warte auf Verbindung auf Port {0}...", listen.LocalEndpoint);
            using (TcpClient client = listen.AcceptTcpClient()) {
                Console.WriteLine("Verbindung zu {0}", client.Client.RemoteEndPoint);
                StreamWriter sw = new StreamWriter(client.GetStream());
                sw.WriteLine("Zur Zeit: {0}", DateTime.Now.ToString());
                sw.WriteLine("bist Du: {0}", client.Client.RemoteEndPoint);
                sw.WriteLine("bin ich: {0}", client.Client.LocalEndPoint);
                sw.Flush();
            }
        }
    }
}