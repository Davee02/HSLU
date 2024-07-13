﻿// ----------------------------------------------------------------------------
// CSA - C# in Action
// (c) 2020, Christian Jost, HSLU
// ----------------------------------------------------------------------------
using System;

namespace Explorer700Library
{
    public class KeyEventArgs : EventArgs
    {
        public KeyEventArgs(Keys keys)
        {
            Keys = keys;
        }

        public Keys Keys { get; }
    }
}
