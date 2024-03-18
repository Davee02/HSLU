class HelloWorld
{
    static void Main(string[] args)
    {
        PrintMessage("Hello World", false);
        PrintMessage("Hello World", true);
        Console.Read();
    }

    private static void PrintMessage(string msg, bool upperCase)
    {
        if (upperCase)
        {
            msg = msg.ToUpper();
        }
        Console.WriteLine(msg);
    }
}
