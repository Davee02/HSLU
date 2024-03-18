// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2021, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;

namespace Explorer700Library
{
    [Flags]
    public enum Keys
    {
        NoKey = 0,
        Up = 2,
        Down = 4,
        Left = 1,
        Right = 8,
        Center = 16
    }
}
