// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2024, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Device.Gpio;
using System.Diagnostics;
using System.Threading;

namespace Explorer700Library
{
    public class Joystick
    {
        private const byte BIT_DOWN = 2;
        private const byte BIT_LEFT = 0;
        private const byte BIT_UP = 1;
        private const byte BIT_RIGHT = 3;

        #region members & events
        private int centerPin;
        public event EventHandler<KeyEventArgs> JoystickChanged;
        #endregion

        #region constructor & destructor
        public Joystick(Pcf8574 pcf8574, GpioController gpioController)
        {
            Pcf8574 = pcf8574;
            pcf8574.Mask |= 0x0F;
            centerPin = 20;
            GpioController = gpioController;
            GpioController.OpenPin(centerPin, PinMode.InputPullUp);

            // Start Polling-Thread
            Thread t = new Thread(Run);
            t.IsBackground = true;
            t.Start();
        }
        #endregion

        #region properties
        private Pcf8574 Pcf8574 { get; set; }

        internal GpioController GpioController { get; }

        /// <summary>
        /// Liest und liefert den Zustand des Joysticks
        /// </summary>
        public Keys Keys
        {
            get
            {
                Keys k = Keys.NoKey;
 
                var down = !Pcf8574[BIT_DOWN];
                var left = !Pcf8574[BIT_LEFT];
                var up = !Pcf8574[BIT_UP];
                var right = !Pcf8574[BIT_RIGHT];

                if (down) k |= Keys.Down;
                if (left) k |= Keys.Left;
                if (up) k |= Keys.Up;
                if (right) k |= Keys.Right;

                if (!(bool)GpioController.Read(centerPin)) k |= Keys.Center;

                return k;
            }
        }
        #endregion

        #region methods
        /// <summary>
        /// Pollt alle 50ms den Joystick und generiert ein JoystickChanged Event, falls
        /// sich der Zustand des Joysticks (Taste gedrückt/losgelassen) verändert hat.
        /// </summary>
        private void Run()
        {
            Keys oldState = Keys;
            while (true)
            {
                Thread.Sleep(50);
                var newKeys = Keys;
                if (oldState != newKeys)
                {
                    oldState = newKeys;
                    JoystickChanged?.Invoke(this, new KeyEventArgs(newKeys));
                }
            }
        }
        #endregion
    }
}
