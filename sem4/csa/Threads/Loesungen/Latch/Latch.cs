using System.Threading;

namespace Latch {

    class Latch : ISynch {

        private readonly EventWaitHandle signal = new ManualResetEvent(false);
        public void Acquire() {
            signal.WaitOne();
        }
        public void Release() {
            signal.Set();
        }
    }
}