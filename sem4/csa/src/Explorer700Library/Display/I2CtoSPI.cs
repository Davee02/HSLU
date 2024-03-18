// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2021, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Device.Spi;
using System.Reflection;

namespace Explorer700Library
{
    public class I2CtoSPI : II2CDevice
    {
        private readonly object syncLock = new object();
        private readonly SpiDevice dev;

        internal I2CtoSPI(int deviceId, int fileDescriptor)
        {
            //Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            DeviceId = deviceId;
            FileDescriptor = fileDescriptor;

            SpiConnectionSettings settings = new SpiConnectionSettings(0);
            settings.ClockFrequency = 900000;
            dev = SpiDevice.Create(settings);
        }

        public int DeviceId { get; }

        public int FileDescriptor { get; }

        public byte Read()
        {
            Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            throw new NotImplementedException();
        }

        public byte[] Read(int length)
        {
            Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            throw new NotImplementedException();
        }

        public byte ReadAddressByte(int address)
        {
            Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            throw new NotImplementedException();
        }

        public ushort ReadAddressWord(int address)
        {
            Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            throw new NotImplementedException();
        }

        public void Write(byte data)
        {
            Console.WriteLine(MethodInfo.GetCurrentMethod().Name + " 1:");
            throw new NotImplementedException();
        }

        public void Write(byte[] data)
        {
            //Console.WriteLine(MethodInfo.GetCurrentMethod().Name + " 2");

            lock (syncLock)
            {
                ReadOnlySpan<byte> buf = new ReadOnlySpan<byte>(data);
                dev.Write(buf);
                //var result = WiringPi.WiringPiSPIDataRW(0, data, data.Length);
            }
        }

        public void WriteAddressByte(int address, byte data)
        {
            Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            throw new NotImplementedException();
        }

        public void WriteAddressWord(int address, ushort data)
        {
            Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            throw new NotImplementedException();
        }
    }
}
