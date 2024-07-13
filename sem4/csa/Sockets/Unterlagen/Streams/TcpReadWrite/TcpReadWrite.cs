using System;
using System.Net.Sockets;
using System.IO;

namespace TcpReadWrite; 
class TcpReadWrite {
    public static void Main() {
        using (TcpClient client = new TcpClient("post.ch", 80)) {
            StreamWriter outStream = new StreamWriter(client.GetStream());
            StreamReader inStream = new StreamReader(client.GetStream());
            outStream.WriteLine("GET / HTTP1.1");
            outStream.WriteLine();
            outStream.Flush();
            String line;
            while ((line = inStream.ReadLine()) != null) {
                Console.WriteLine(line);
            }
        }
    }
}