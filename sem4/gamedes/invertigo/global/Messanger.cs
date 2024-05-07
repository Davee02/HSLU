using Godot;
using System;

public partial class Messanger : Node
{
    private static Messanger _instance;

    [Signal]
    public delegate void GravitySwitchedEventHandler();

    [Signal]
    public delegate void LevelCompletedEventHandler();

    public static Messanger Instance
    {
        get
        {
            if (_instance == null)
            {
                _instance = new Messanger();
            }

            return _instance;
        }
    }
}
