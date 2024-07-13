using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace NebenlaeufigerServer; 
public class EchoServer {
    public static void Main() {
        IPAddress ipAddress = Dns.GetHostEntry("localhost").AddressList[0];
        TcpListener listen = new TcpListener(ipAddress, 7777);
        listen.Start();
        while (true) {
            Console.WriteLine("Warte auf Verbindung auf Port {0}...", listen.LocalEndpoint);
            TcpClient client = listen.AcceptTcpClient();
            Console.WriteLine("Echo Handler für {0} erzeugen und starten", client.Client.RemoteEndPoint);
            EchoHandler handler = new EchoHandler(client);
            new Thread(handler.DoEcho).Start();
        }
    }
}