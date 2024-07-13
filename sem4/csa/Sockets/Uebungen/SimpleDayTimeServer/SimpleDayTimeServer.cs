using System;
using System.Net.Sockets;
using System.IO;

namespace SimpleDayTimeServer {

    public class SimpleDayTimeServer {

        public static void Main() {
            TcpListener listen = new TcpListener(13);
            listen.Start();
            while (true) {
                Console.WriteLine("Warte auf Verbindung auf Port " +
                    listen.LocalEndpoint + "...");
                TcpClient client = listen.AcceptTcpClient();
                Console.WriteLine("Verbindung zu " + client.Client.RemoteEndPoint);
                TextWriter tw = new StreamWriter(client.GetStream());
                tw.Write(DateTime.Now.ToString());
                tw.Flush();
                client.Close();
            }
        }
    }
}