// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2023, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Device.I2c;

namespace Explorer700Library
{
    public class Pcf8574
    {
        #region members
        private byte data;
        private byte mask;
        private readonly I2cDevice dev;
        #endregion

        #region constructor & destructor
        public Pcf8574(int address)
        {
            I2cBus bus = I2cBus.Create(1);
            dev = bus.CreateDevice(address);
        }
        #endregion

        #region properties
        /// <summary>
        /// Setzt eine Maske die dazu führt, dass ausgewählte Bits nie auf 0 gesetzt werden.
        /// </summary>
        public byte Mask
        {
            get { return this.mask; }
            set
            {
                this.mask = value;
                //Write(data);
            }
        }
        #endregion

        #region indexer
        public bool this[int bit]
        {
            get { return (Read() & (1 << bit)) != 0; }
            set { Write((byte)(value ? data | (1 << bit) : data & ~(1 << bit))); }
        }
        #endregion

        #region methods
        /// <summary>
        /// Liest den Zustand der Port-Pins.
        /// </summary>
        /// <returns>1 Byte mit den 8 Zuständen des Ports</returns>
        public byte Read()
        {
            data = dev.ReadByte();
            return data;
        }

        /// <summary>
        /// Setzt die 8 Pins des Port Expanders auf High oder Low
        /// </summary>
        /// <param name="data">1 Byte mit den 8 Zuständen</param>
        public void Write(byte data)
        {
            this.data = data;
            dev.WriteByte((byte)(data | mask));
        }
        #endregion
    }
}
