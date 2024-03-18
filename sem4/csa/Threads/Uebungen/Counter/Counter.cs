namespace Counter;
using System.Threading;

class Counter
{

    private int count = 0;
    public int NextNumber()
    {
        count++;
        return count;
    }
}