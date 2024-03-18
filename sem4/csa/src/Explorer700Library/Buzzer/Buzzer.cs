// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2024, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Threading;

namespace Explorer700Library
{
    public class Buzzer
    {
        private const byte BIT_BUZZER = 7;

        public Buzzer(Pcf8574 pcf8574)
        {
            Pcf8574 = pcf8574;
            AppDomain.CurrentDomain.ProcessExit += delegate (Object o, EventArgs e) { pcf8574[7] = true; };
            AppDomain.CurrentDomain.UnhandledException += delegate (Object o, UnhandledExceptionEventArgs e) { pcf8574[7] = true; };
        }

        /// <summary>
        /// Property für den Zugriff auf den PCF8574
        /// </summary>
        private Pcf8574 Pcf8574 { get; set; }

        /// <summary>
        /// Schaltet den Buzzer ein-/aus bzw. liefert den Zustand ob er eingeschaltet (=true) ist.
        /// </summary>
        public bool Enabled
        {
            get { return !Pcf8574[BIT_BUZZER]; }
            set { Pcf8574[BIT_BUZZER] = !value; }
        }

        /// <summary>
        /// Schaltet den Piepser für eine bestimmte Zeit ein und anschliessend wieder aus (Piepston)
        /// </summary>
        /// <param name="timeMs">Spieldauer in Millisekunden</param>
        public void Beep(int timeMs)
        {
            if (timeMs < 0) throw new ArgumentOutOfRangeException("timeMs");
            Enabled = true;
            Thread.Sleep(timeMs);
            Enabled = false;
        }
    }
}
