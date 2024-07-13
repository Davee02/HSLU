using System;
using System.Net.Sockets;
using System.IO;

namespace SimpleDayTimeServer {

    public class TimeHandler {

        private readonly TcpClient client;

        public TimeHandler(TcpClient client) {
            this.client = client;
        }
        public void Do() {
            Console.WriteLine("Verbindung zu " + client.Client.RemoteEndPoint);
            TextWriter tw = new StreamWriter(client.GetStream());
            tw.Write(DateTime.Now.ToString());
            tw.Flush();
            client.Close();
        }
    }
}