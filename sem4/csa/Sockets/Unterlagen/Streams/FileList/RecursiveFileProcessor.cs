// For Directory.GetFiles and Directory.GetDirectories
// For File.Exists, Directory.Exists
using System;
using System.IO;
using System.Collections;

namespace FileList {
    public class RecursiveFileProcessor {
        public static void Main(string[] args) {
            if (args.Length == 0) {
                // Projektverzeichnis unter Windows
                string projectDirectory = Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName;
                ProcessDirectory(projectDirectory);
            } else {
                string path = args[0];
                if (File.Exists(path)) {
                    // This path is a file
                    ProcessFile(path);
                }
                else if (Directory.Exists(path)) {
                    // This path is a directory
                    ProcessDirectory(path);
                }
                else {
                    Console.WriteLine("{0} is not a valid file or directory.", path);
                }
            }
        }

        public static void ProcessDirectory(string targetDirectory) {
            string[] fileEntries = Directory.GetFiles(targetDirectory);
            foreach (string fileName in fileEntries) {
                ProcessFile(fileName);
            }
            string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
            foreach (string subdirectory in subdirectoryEntries) {
                ProcessDirectory(subdirectory);
            }
        }
        public static void ProcessFile(string path) {
            Console.WriteLine("Processed file '{0}'.", path);
        }
    }
}
