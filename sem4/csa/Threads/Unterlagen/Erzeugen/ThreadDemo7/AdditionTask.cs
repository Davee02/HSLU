using System;

namespace ThreadDemos;

class AdditionTask
{

    private readonly int n;
    private readonly string id;

    public AdditionTask(string id, int n)
    {
        this.id = id;
        this.n = n;
    }
    public void Add()
    {
        long sum = 0;
        for (int i = 0; i <= n; i++)
        {
            sum += i;
        }
        Console.WriteLine("{0}: SUM ({1}) -> {2}", id, n, sum);
    }
}