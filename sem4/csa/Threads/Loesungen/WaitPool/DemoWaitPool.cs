using System;
using System.Threading;

namespace WaitPool {

    class DemoWaitPool {

        static void Main() {
            Object synch = new Object();
            MyTask myThread = new MyTask(synch);
            new Thread(myThread.Run).Start();
            Thread.Sleep(1000);
            lock (synch) {
                Monitor.Pulse(synch);
            }
        }
    }
}
