using Godot;

public partial class level_handler : Node
{
    private int _currentLevel;
    private main_character _mainCharacter;
    private end_screen _endScreen;
    private Node _levelNode;
    private AudioStreamPlayer _finishLevelAudioPlayer;

    [Export]
    public int StartWithLevel { get; set; }

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.LevelCompleted, Callable.From(OnLevelCompleted));
        Messanger.Instance.Connect(Messanger.SignalName.CharacterDied, Callable.From(OnCharacterDied));
        Messanger.Instance.Connect(Messanger.SignalName.GameRestarted, Callable.From(OnGameRestarted));
        Messanger.Instance.Connect(Messanger.SignalName.GameStarted, Callable.From(OnGameStarted));

        _levelNode = GetNode<Node>("Level");
        _mainCharacter = GetNode<main_character>("/root/Main/Game/MainCharacter");
        _endScreen = GetNode<end_screen>("/root/Main/GUI/EndScreen");
        _finishLevelAudioPlayer = GetNode<AudioStreamPlayer>("FinishLevelAudioPlayer");

        _currentLevel = StartWithLevel;
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
        _finishLevelAudioPlayer.Play();
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
            _finishLevelAudioPlayer.Finished += () => { Messanger.Instance.EmitSignal(Messanger.SignalName.GameFinished); };
            return;
        }

        var currentLevelScene = ResourceLoader.Load<PackedScene>(currentLevelScenePath);
        var instance = currentLevelScene.Instantiate<base_level>();

        if (instance.StartWithFlippedGravity)
        {
            Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToInverted);
        }
        else
        {
            Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToNormal);
        }
        _mainCharacter.Position = instance.CharacterStartPosition;
        _mainCharacter.Velocity = Vector2.Zero;

        _levelNode.CallDeferred(MethodName.AddChild, instance);
    }

    private void OnCharacterDied()
    {
        GD.Print("Received character died signal");
        LoadLevel(); // reload the current level to restart it
    }

    private void OnGameStarted()
    {
        LoadLevel();
    }

    private void RestartLevel()
    {
        GD.Print("Restarting level");
        Messanger.Instance.EmitSignal(Messanger.SignalName.CharacterDied);
    }
}
