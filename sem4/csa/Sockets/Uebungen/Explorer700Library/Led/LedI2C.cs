using System;
using System.Collections.Generic;
using System.Text;

namespace Explorer700Library.Led
{
    public class LedI2C : LedBase
    {

        const int BIT_LED2 = 4;


        public LedI2C(Pcf8574 pcf8574)
        {
            Led = Leds.Led2;
            Pcf8574 = pcf8574;
        }

        public Pcf8574 Pcf8574 { get;}

        public override Leds Led { get; }

        public override bool Enabled
        {
            get { return !Pcf8574[BIT_LED2]; }
            set { Pcf8574[BIT_LED2] = !value; }
        }
    }
}
