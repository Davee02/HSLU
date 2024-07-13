using System;
using System.Threading;

namespace LostSignals {

    class AWait : ISynch {

        private readonly Semaphore sema = null;
        public AWait(int n) {
            sema = new Semaphore(0, n);
        }
        public void Acquire() {
            sema.WaitOne();
        }
        public void Release() {
            sema.Release();
        }
    }
}