using System;
using System.Net.Sockets;

namespace SocketInfo; 

public class SocketInfo {

    public static void Main(string[] args) {
        Console.WriteLine("Socket Information");
        for (int i = 0; i < args.Length; i++) {
            try {
                TcpClient theClient = new TcpClient(args[i], 80);
                Socket theSocket = theClient.Client;
                Console.WriteLine("Der lokale Host ({0}) ist verbunden mit", theSocket.LocalEndPoint);
                Console.WriteLine("dem entfernten Host {0} ({1})", args[i], theSocket.RemoteEndPoint);
                Console.WriteLine("ueber einen {0} Socket.", theSocket.ProtocolType);
                theClient.Close();
            }
            catch (Exception e) {
                Console.Error.WriteLine(e.Message);
            }
        }
    }
}