using System;
using System.Threading;

namespace WaitPool {

    class MyTask {

        private readonly object synch;

        public MyTask(object synch) {
            this.synch = synch;
        }
        public void Run() {
            Console.WriteLine("warten...");
            lock (synch) {
                Monitor.Wait(synch);
            }
            Console.WriteLine("...aufgewacht");
        }
    }
}