// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2020, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Reflection;
using Unosquare.RaspberryIO.Abstractions;
using Unosquare.WiringPi.Native;

namespace Explorer700Library
{
    public class I2CtoSPI : II2CDevice
    {
        private readonly object syncLock = new object();

        internal I2CtoSPI(int deviceId, int fileDescriptor)
        {
            //Console.WriteLine(MethodInfo.GetCurrentMethod().Name);
            DeviceId = deviceId;
            FileDescriptor = fileDescriptor;

            WiringPi.WiringPiSPISetup(0, 976000);
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
            //lock (syncLock)
            //{
            //    byte[] b = { 0 };
            //    b[0] = data;
            //    var result = WiringPi.WiringPiSPIDataRW(0, b, b.Length);
            //}
        }

        public void Write(byte[] data)
        {
            //Console.WriteLine(MethodInfo.GetCurrentMethod().Name + " 2");

            lock (syncLock)
            {
                var result = WiringPi.WiringPiSPIDataRW(0, data, data.Length);
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
