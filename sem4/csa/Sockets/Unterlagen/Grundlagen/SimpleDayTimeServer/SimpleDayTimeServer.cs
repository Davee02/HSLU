using System;
using System.Net.Sockets;
using System.IO;
using System.Net;

namespace SimpleDayTimeServer; 

public class SimpleDayTimeServer {

    public static void Main() {
        // 1.
        //TcpListener listen = new TcpListener(1313);
        // 2.
        //IPAddress ipAddress = Dns.Resolve(Dns.GetHostName()).AddressList[0];
        //IPEndPoint ipLocalEndPoint = new IPEndPoint(ipAddress, 13);
        //TcpListener listen = new TcpListener(ipLocalEndPoint);
        // 3.
        IPAddress ipAddress = Dns.GetHostEntry("localhost").AddressList[0];
        TcpListener listen = new TcpListener(IPAddress.Parse("192.168.1.149"), 1313);
        // 4.
        //TcpListener listen = new TcpListener(IPAddress.Any,1313);
        listen.Start();
        while (true) {
            Console.WriteLine("Warte auf Verbindung auf Port {0}...", listen.LocalEndpoint);
            TcpClient client = listen.AcceptTcpClient();
            Console.WriteLine("Verbindung zu {0}", client.Client.RemoteEndPoint);
            TextWriter tw = new StreamWriter(client.GetStream());
            tw.Write(DateTime.Now.ToString());
            tw.Flush();
            client.Close();
        }
    }
}