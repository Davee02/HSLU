namespace ThreadBeenden;

class ThreadBeenden1
{

    static void Main()
    {
        try
        {
            new Thread(Go).Start();
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception! " + ex.Message);
        }
        // mache was anderes
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine("for loop {0}", i);
            Thread.Sleep(200);
        }
    }
    static void Go()
    {
        throw null;    // NullReferenceException wird ausgel�st
        Console.WriteLine("uups!");
    }
}