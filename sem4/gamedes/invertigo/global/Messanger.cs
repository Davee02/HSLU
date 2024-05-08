using Godot;

public partial class Messanger : Node
{
    private static Messanger _instance;

    [Signal]
    public delegate void GravitySwitchedEventHandler();

    [Signal]
    public delegate void LevelCompletedEventHandler();

    [Signal]
    public delegate void CharacterDiedEventHandler();

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
