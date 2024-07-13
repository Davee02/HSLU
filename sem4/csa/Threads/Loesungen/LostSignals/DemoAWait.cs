using System.Threading;

namespace LostSignals {

    class DemoAWait {

        static void Main() {
            ISynch signal = new AWait(Operator.MAXCOUNT);
            Operator op = new Operator(signal);
            new Thread(op.Do).Start();
            for (int i = 0; i < 10; i++) {
                Worker worker = new Worker(signal, op, "Worker" + i);
                new Thread(worker.Do).Start();
            }
        }
    }
}