using System;
using System.Threading;

namespace Latch {

    class RaceHorse {

        private readonly ISynch startSignal;
        private readonly int nr;

        public RaceHorse(int nr, ISynch startSignal) {
            this.nr = nr;
            this.startSignal = startSignal;
        }
        public void Run() {
            Console.WriteLine("Rennpferd " + nr + " geht in die Startbox.");
            startSignal.Acquire();
            Console.WriteLine("Rennpferd " + nr + " läuft los.");
            Thread.Sleep(new Random().Next(3000));
            Console.WriteLine("Rennpferd " + nr + " ist im Ziel.");
        }
    }
}