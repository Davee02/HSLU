using Godot;

public partial class LevelHandler : Node
{
    private int _currentLevel;
    private Level _levelNode;
    private main_character _mainCharacter;
    private end_screen _endScreen;

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.LevelCompleted, Callable.From(OnLevelCompleted));
        Messanger.Instance.Connect(Messanger.SignalName.CharacterDied, Callable.From(OnCharacterDied));
        Messanger.Instance.Connect(Messanger.SignalName.GameRestarted, Callable.From(OnGameRestarted));

        _levelNode = GetNode<Level>("/root/Main/Level");
        _mainCharacter = GetNode<main_character>("/root/Main/MainCharacter");
        _endScreen = GetNode<end_screen>("/root/Main/GUI/EndScreen");

        _currentLevel = _levelNode.StartWithLevel;

        LoadLevel();
    }

    public override void _Process(double delta)
    {
        if (Input.IsActionJustPressed("reset"))
        {
            RestartLevel();
        }
    }

    public void OnLevelCompleted()
    {
        GD.Print("Received level completed signal");
        _currentLevel++;
        LoadLevel();
    }

    public void OnGameRestarted()
    {
        GD.Print("Received game restarted signal");
        _currentLevel = 1;
        LoadLevel();
    }

    private void LoadLevel()
    {
        if (_levelNode.GetChildCount() > 0)
        {
            GD.Print($"Removing child {_levelNode.GetChild(0).Name}");
            _levelNode.GetChild(0).QueueFree();
        }

        var currentLevelScenePath = $"res://scenes/game/levels/level_{_currentLevel}.tscn";
        if (!ResourceLoader.Exists(currentLevelScenePath))
        {
            GD.Print($"Level {_currentLevel} does not exist. Assuming it was the last.");
            Messanger.Instance.EmitSignal(Messanger.SignalName.GameFinished);
            return;
        }

        var currentLevelScene = ResourceLoader.Load<PackedScene>(currentLevelScenePath);
        var instance = currentLevelScene.Instantiate<base_level>();

        if(instance.StartWithFlippedGravity)
        {
            Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToInverted);
        }
        else
        {
            Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToNormal);
        }
        _mainCharacter.Position = instance.CharacterStartPosition;
        _mainCharacter.Velocity = Vector2.Zero;

        _levelNode.CallDeferred(Level.MethodName.AddChild, instance);
    }

    private void OnCharacterDied()
    {
        GD.Print("Received character died signal");
        LoadLevel(); // reload the current level to restart it
    }

    public void RestartLevel()
    {
        GD.Print("Restarting level");

        Messanger.Instance.EmitSignal(Messanger.SignalName.CharacterDied);
    }
}
