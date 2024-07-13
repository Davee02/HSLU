// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2020, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.Text;
using System.Threading;
using Unosquare.RaspberryIO;
using Unosquare.RaspberryIO.Abstractions;
using Unosquare.RaspberryIO.Peripherals;

namespace Explorer700Library
{
    public class Display
    {
        private SSD1306 disp;

        private IGpioPin cs;
        private IGpioPin res;
        private IGpioPin dnc;
        private Bitmap bitmap;


        public Display()
        {
            cs = Pi.Gpio[P1.Pin24];                 // GPIO8 = Pin 24
            cs.PinMode = GpioPinDriveMode.Output;   // use pin as ouptut pin
            cs.Write(false);

            res = Pi.Gpio[P1.Pin35];                // GPI19 = Pin 35
            res.PinMode = GpioPinDriveMode.Output;  // use pin as ouptut pin
            res.Write(true);
            Thread.Sleep(10);
            res.Write(false);
            Thread.Sleep(10);
            res.Write(true);

            dnc = Pi.Gpio[P1.Pin36];                // GPI16 = Pin 36
            dnc.PinMode = GpioPinDriveMode.Output;  // use pin as ouptut pin
            dnc.Write(false);

            I2CtoSPI spiDevice = new I2CtoSPI(0, 0);
            disp = new SSD1306(spiDevice,
                SSD1306.DisplayModel.Display128X64, SSD1306.VccSourceMode.Switching);

            bitmap = new Bitmap(128, 64);
            Graphics = Graphics.FromImage(bitmap);
        }



        public Graphics Graphics
        {
            get;
        }


        public void Update()
        {
            disp.LoadBitmap(bitmap, 0.5, 0, 0);

            dnc.Write(false);
            disp.SetAddressRange();
            dnc.Write(true);
            disp.Render();
        }


        public void Clear()
        {
            Graphics.Clear(Color.Black);
            Update();
        }


        /*
        public void Test_()
        {
            for (int i = 0; i < 10; i++)
            {
                Stopwatch sw = Stopwatch.StartNew();

                disp.ClearPixels();
                Update();

                Bitmap btm = new Bitmap(Image.FromFile("./Ressources/test.png"));
                //Bitmap btm = new Bitmap(128, 64);
                Graphics myGraphics = Graphics.FromImage(btm);
                Pen pen = new Pen(Brushes.Black);
                myGraphics.DrawEllipse(pen, -10, -10, 30, 30);
                myGraphics.DrawEllipse(pen, 30, 10, 10, 10);
                pen.Width = 2;
                myGraphics.DrawBezier(pen, new Point(10, 30), new Point(30, 30), new Point(70, 40), new Point(75, 5));
                myGraphics.DrawString("Hello from .NET Core :-)", new Font(new FontFamily("arial"), 8, FontStyle.Regular), Brushes.Black, new PointF(5, 50));

                disp.LoadBitmap(btm, 0.5, 0, 0);

                Update();
                sw.Stop();
                Console.WriteLine(sw.ElapsedMilliseconds);

                Thread.Sleep(10);
            }

            disp.ClearPixels();
            Update();
        }
        */

    }
}
