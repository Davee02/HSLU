using System;
using System.Threading;

namespace LostSignals; 

class Worker {

    private readonly ISynch signal;
    private readonly Operator op;
    private readonly string id;

    public Worker(ISynch signal, Operator op, string id) {
        this.signal = signal;
        this.op = op;
        this.id = id;
    }
    public void Do() {
        while (true) {
            signal.Acquire();
            Console.WriteLine("{0} released...", id);
            Thread.Sleep(op.Operation());
            op.Done(id);
        }
    }
}