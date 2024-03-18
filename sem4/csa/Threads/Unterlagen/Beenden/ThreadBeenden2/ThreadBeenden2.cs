namespace ThreadBeenden;

class ThreadBeenden2
{
    static void Main()
    {
        new Thread(GoX).Start();
        new Thread(GoY).Start();
        Console.WriteLine("finished!");
    }
    static void GoX()
    {
        try
        {
            for (int i = 0; i < 10; i++)
            {
                Console.Write("X");
                if (i == 2)
                {
                    throw null;    // NullReferenceException wird ausgel�st
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception! {0}", ex.Message);
        }
    }
    static void GoY()
    {
        try
        {
            for (int i = 0; i < 10; i++)
            {
                Console.Write("Y");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception! {0}", ex.Message);
        }
    }
}