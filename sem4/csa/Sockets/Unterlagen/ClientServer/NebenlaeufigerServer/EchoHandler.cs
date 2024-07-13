using System;
using System.Net.Sockets;
using System.IO;

namespace NebenlaeufigerServer; 
public class EchoHandler {

    private TcpClient client;

    public EchoHandler(TcpClient client) {
        this.client = client;
    }
    public void DoEcho() {
        StreamReader sr = new StreamReader(client.GetStream());
        StreamWriter sw = new StreamWriter(client.GetStream());
        try {
            while (client.Connected) {
                // Zeichen des Clients empfangen
                Char ch = (char)sr.Read();
                // Zeichen an den Clients senden
                sw.Write(ch);
                sw.Flush();
            }
        }
        catch (Exception ex) {
            Console.WriteLine(ex.Message);
        }
        finally {
            client.Close();
        }
    }
}