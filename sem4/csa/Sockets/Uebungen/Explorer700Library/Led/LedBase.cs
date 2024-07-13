using System;
using System.Collections.Generic;
using System.Text;

namespace Explorer700Library
{
    public abstract class LedBase
    {
        public abstract Leds Led { get; }

        public abstract bool Enabled { get; set; }

        public void Toggle()
        {
            Enabled = !Enabled;
        }

    }
}
