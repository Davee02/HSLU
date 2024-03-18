using System;
using System.Threading;

namespace WaitPool; 

class MyThread {

    private readonly object synch;

    public MyThread(object synch) {
        this.synch = synch;
    }
    public void Run() {
        Console.WriteLine("warten...");
        lock (synch) {
            Monitor.Wait(this);
        }
        Console.WriteLine("...aufgewacht");
    }
}