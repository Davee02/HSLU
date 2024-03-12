// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2024, Christian Jost, HSLU
// ----------------------------------------------------------------------------

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
