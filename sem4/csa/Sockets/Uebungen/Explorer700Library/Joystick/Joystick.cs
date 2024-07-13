// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2020, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Diagnostics;
using System.Threading;
using Unosquare.RaspberryIO;
using Unosquare.RaspberryIO.Abstractions;

namespace Explorer700Library
{
    public class Joystick
    {
        #region members & events
        private IGpioPin centerPin;
        public event EventHandler<KeyEventArgs> JoystickChanged;
        #endregion

        #region constructor & destructor
        public Joystick(Pcf8574 pcf8574)
        {
            Pcf8574 = pcf8574;
            pcf8574.Mask |= 0x0F;
            centerPin = Pi.Gpio[20];
            centerPin.PinMode = GpioPinDriveMode.Input;
            centerPin.InputPullMode = GpioPinResistorPullMode.PullUp;

            // Bugfix da die folgenden Zeile nicht funktioniert:
            // centerPin.InputPullMode = GpioPinResistorPullMode.PullUp;
            // Console.Write("   " + centerPin.Read() + "   ");
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "/usr/bin/raspi-gpio";
            psi.Arguments = "set 20 ip pu";
            Process.Start(psi);

            // Start Polling-Thread
            Thread t = new Thread(Run);
            t.IsBackground = true;
            t.Start();
        }
        #endregion

        #region properties
        private Pcf8574 Pcf8574 { get; set; }

        /// <summary>
        /// Liest und liefert den Zustand des Joysticks
        /// </summary>
        public Keys Keys
        {
            get
            {
                byte data = Pcf8574.Read();
                data = (byte)((~data) & 0x0F);
                Keys k = (Keys)data; // Low Active
                if (!centerPin.Read()) k |= Keys.Center;
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
                Keys newState = Keys;
                if (oldState != newState)
                {
                    JoystickChanged?.Invoke(this, new KeyEventArgs(newState));
                    oldState = newState;
                }
                Thread.Sleep(50);
            }
        }
        #endregion
    }
}
