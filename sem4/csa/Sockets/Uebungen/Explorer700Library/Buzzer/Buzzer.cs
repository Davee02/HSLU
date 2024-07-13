using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;

namespace Explorer700Library
{
    public class Buzzer
    {
        private const byte BIT_BUZZER = 7;

        public Buzzer(Pcf8574 pcf8574)
        {
            Pcf8574 = pcf8574;

            AppDomain.CurrentDomain.ProcessExit += delegate (Object o, EventArgs e)
            {
                Pcf8574[7] = true;
            };
        }

        private Pcf8574 Pcf8574 { get; set; }

        public bool Enabled
        {
            get { return !Pcf8574[BIT_BUZZER]; }
            set { Pcf8574[BIT_BUZZER] = !value; }
        }

        public void Beep(int timeMs)
        {
            if (timeMs < 0) throw new ArgumentOutOfRangeException("timeMs");
            Enabled = true;
            Thread.Sleep(timeMs);
            Enabled = false;
        }
    }
}
