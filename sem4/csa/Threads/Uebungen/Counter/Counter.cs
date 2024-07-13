namespace Counter;
using System.Threading;

class Counter
{
    private readonly static object lockObject = new object();
    private int count = 0;
    public int NextNumber()
    {
        lock (lockObject)
        {
            count++;
            return count;
        }
    }
}