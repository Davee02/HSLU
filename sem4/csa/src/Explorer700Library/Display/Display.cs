// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2023, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;
using System.Collections.Generic;
using System.Device.Gpio;
using System.Diagnostics;
using System.Drawing;
using System.Text;
using System.Threading;

namespace Explorer700Library
{
    public class Display
    {
        private SSD1306 disp;

        private int cs;
        private int res;
        private int dnc;
        private Bitmap bitmap;


        public Display(GpioController gpioController)
        {
            GpioController = gpioController;

            cs = 8;                                         // GPIO8 = Pin 24
            GpioController.OpenPin(cs, PinMode.Output);     // use pin as ouptut pin
            GpioController.Write(cs, true);

            res = 19;                                       // GPI19 = Pin 35
            GpioController.OpenPin(res, PinMode.Output);    // use pin as ouptut pin
            GpioController.Write(res, true);
            Thread.Sleep(10);
            GpioController.Write(res, false);
            Thread.Sleep(10);
            GpioController.Write(res, true);
            
            Thread.Sleep(50);
            GpioController.Write(cs, false);

            dnc = 16;                                       // GPI16 = Pin 36
            GpioController.OpenPin(dnc, PinMode.Output);    // use pin as ouptut pin
            GpioController.Write(dnc, false);

            I2CtoSPI spiDevice = new I2CtoSPI(0, 0);
            disp = new SSD1306(spiDevice,
                SSD1306.DisplayModel.Display128X64, SSD1306.VccSourceMode.Switching);

            bitmap = new Bitmap(128, 64);
            Graphics = Graphics.FromImage(bitmap);
            AppDomain.CurrentDomain.ProcessExit += delegate (Object o, EventArgs e) { Clear(); };
            AppDomain.CurrentDomain.UnhandledException += delegate (Object o, UnhandledExceptionEventArgs e) { Clear(); };
        }

        internal GpioController GpioController { get; }



        public Graphics Graphics
        {
            get;
        }


        public void Update()
        {
            disp.LoadBitmap(bitmap, 0.5, 0, 0);
            GpioController.Write(dnc, false);
            disp.SetAddressRange();
            GpioController.Write(dnc, true);
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
