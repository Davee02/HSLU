using System.Threading;

namespace Counter {

    class Counter {

        private int count = 0;
        private readonly object locker = new object();
        public int NextNumber() {
            lock (locker) {
                count++;
                Thread.Yield();
                return count;
            }
        }
    }
}
