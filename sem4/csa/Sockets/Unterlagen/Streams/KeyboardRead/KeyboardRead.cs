using System;

namespace KeyboardRead {
    class KeyboardRead {
        public static void Main() {
            string line;
            Console.Write("Bitte Eingabe: ");
            while ((line = Console.ReadLine()) != null) {
                Console.WriteLine("Eingabe war  : " + line);
                Console.Write("Bitte Eingabe: ");
            }
        }
    }
}