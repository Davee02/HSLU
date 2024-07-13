using System;
using System.Net.Sockets;
using System.IO;
using System.Threading;

namespace SimpleHttpServer {

    public class SimpleHttpServer {

        public static void Main() {
            // Projektverzeichnis unter Windows
            string projectDirectory = Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName;
            Console.WriteLine("Content: {0}", projectDirectory);
        }
    }
}
