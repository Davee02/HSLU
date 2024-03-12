using Explorer700Library;
using System;
using System.Drawing;
using System.IO;
using System.Reflection;
using System.Threading;

namespace Explorer700Demo
{
    class Program
    {
        private static Explorer700 exp;

        static void Main(string[] args)
        {
            Console.WriteLine("Start...");
            exp = new Explorer700();

            //Eingebettete Bild Ressource "test.png" laden und auf dem Display darstellen
            var resNames = Assembly.GetExecutingAssembly().GetManifestResourceNames();
            Stream imageStream = Assembly.GetExecutingAssembly().GetManifestResourceStream("Explorer700Demo.Ressources.test.png");
            Image image = Image.FromStream(imageStream);

            Graphics g = exp.Display.Graphics;
            g.DrawImage(image, 0, 0);

            Pen pen = new Pen(Brushes.White);
            g.DrawEllipse(pen, -10, -10, 30, 30);
            g.DrawEllipse(pen, 30, 10, 10, 10);
            pen.Width = 2;
            g.DrawBezier(pen, new Point(10, 30), new Point(30, 30), new Point(70, 40), new Point
            (75, 5));
            g.DrawString("Hello .NET :-)", new Font(new FontFamily("arial"), 8, FontStyle.Bold),
            Brushes.White, new PointF(5, 50));


            exp.Display.Update();


            exp.Joystick.JoystickChanged += (s, e) =>
            {
                Console.WriteLine(e.Keys);
            };

            Console.ReadKey();
        }
    }
}
