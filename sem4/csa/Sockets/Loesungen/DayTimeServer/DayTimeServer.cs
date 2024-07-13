using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace SimpleDayTimeServer {

    public class DayTimeServer {
        // PC Version
        public static void Main() {
            TcpListener listen = new TcpListener(IPAddress.Any, 1300);
            listen.Start();
            while (true) {
                Console.WriteLine("Warte auf Verbindung auf Port " +
                    listen.LocalEndpoint + "...");
                new Thread(new TimeHandler(listen.AcceptTcpClient()).Do).Start();
            }
        }
    }
}