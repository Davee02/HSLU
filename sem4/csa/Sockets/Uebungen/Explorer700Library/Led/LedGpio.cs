using System;
using System.Collections.Generic;
using System.Text;
using Unosquare.RaspberryIO;
using Unosquare.RaspberryIO.Abstractions;

namespace Explorer700Library.Led
{
    public class LedGpio : LedBase
    {

        private IGpioPin ledPin;

        public LedGpio()
        {
            ledPin = Pi.Gpio[26]; // BCM 12
            ledPin.PinMode = GpioPinDriveMode.Output; // use as output
        }


        public override Leds Led => Leds.Led1;


        public override bool Enabled
        {
            get { return ledPin.Read(); }
            set { ledPin.Write(value); }
        }
    }
}
