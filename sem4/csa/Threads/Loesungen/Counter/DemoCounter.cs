using System;
using System.Threading;

namespace Counter {

    class DemoCounter {

        private readonly String id;
        private readonly Counter counter;

        public DemoCounter(String id, Counter counter) {
            this.id = id;
            this.counter = counter;
        }
        void Go() {
            for (int i = 0; i < 10; i++) {
                System.Console.WriteLine(id + counter.NextNumber());
                Thread.Sleep(50);
            }
        }
        static void Main() {
            Counter counter = new();
            DemoCounter ct1 = new("T1: ", counter);
            DemoCounter ct2 = new("T2: ", counter);
            DemoCounter ct3 = new("T3: ", counter);
            new Thread(ct1.Go).Start();
            new Thread(ct2.Go).Start();
            new Thread(ct3.Go).Start();
        }
    }
}
