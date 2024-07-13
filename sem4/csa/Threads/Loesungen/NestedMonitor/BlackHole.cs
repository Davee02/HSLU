using System;

namespace BlackHole {

    class BlackHole {

        private readonly NotifyingQueue<String> queue = new();

        public void Put(String thing) {
            queue.Enqueue(thing);
        }
        public String Get() {
            return queue.Dequeue();
        }
    }
}
