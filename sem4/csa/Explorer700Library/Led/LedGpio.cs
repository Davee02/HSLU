// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2024, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Device.Gpio;

namespace Explorer700Library
{
    public class LedGpio : LedBase
    {
        private readonly int ledPin;

        public LedGpio(GpioController gpioController)
        {
            ledPin = 26;
            GpioController = gpioController;
            GpioController.OpenPin(ledPin, PinMode.Output);
        }

        internal GpioController GpioController { get; }

        public override Leds Led => Leds.Led1;

        public override bool Enabled
        {
            get { return (bool)GpioController.Read(ledPin); }
            set { GpioController.Write(ledPin, value); }
        }
    }
}
