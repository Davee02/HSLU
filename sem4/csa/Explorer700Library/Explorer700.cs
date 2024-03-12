// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2024, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System.Device.Gpio;

namespace Explorer700Library
{
    public class Explorer700
    {
        public Explorer700()
        {
            // GPIO Controller für den Zugriff auf die Hardware initialisieren
            GpioController gpioController = new GpioController();
            Led1 = new LedGpio(gpioController);
            Pcf8574 = new Pcf8574(0x20);
            Led2 = new LedI2C(Pcf8574);
            Buzzer = new Buzzer(Pcf8574);
            Joystick = new Joystick(Pcf8574, gpioController);
            Display = new Display(gpioController);
            Buzzer.Enabled = false;
        }

        public LedBase Led1 { get; }
        public LedBase Led2 { get; }
        private Pcf8574 Pcf8574 { get; }
        public Buzzer Buzzer { get; }
        public Joystick Joystick { get; }
        public Display Display { get; }

    }
}
