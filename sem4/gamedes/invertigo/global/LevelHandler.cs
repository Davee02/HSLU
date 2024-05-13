using Godot;

public partial class LevelHandler : Node
{
    private int _currentLevel;
    private Level _levelNode;
    private main_character _mainCharacter;

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.LevelCompleted, Callable.From(OnLevelCompleted));
        Messanger.Instance.Connect(Messanger.SignalName.CharacterDied, Callable.From(OnCharacterDied));

        _levelNode = GetNode<Level>("/root/Main/Level");
        _currentLevel = _levelNode.StartWithLevel;

        _mainCharacter = GetNode<main_character>("/root/Main/MainCharacter");

        LoadLevel();
    }

    public void OnLevelCompleted()
    {
        GD.Print("Received level completed signal");
        _currentLevel++;
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
            GD.Print($"Level {_currentLevel} does not exist.");
            return;
        }

        var currentLevelScene = ResourceLoader.Load<PackedScene>(currentLevelScenePath);
        var instance = currentLevelScene.Instantiate<base_level>();
        _levelNode.AddChild(instance);

        _mainCharacter.Position = instance.CharacterStartPosition;
        _mainCharacter.SetGravityFlipped(instance.StartWithFlippedGravity);
    }

    private void OnCharacterDied()
    {
        GD.Print("Received character died signal");
        LoadLevel(); // reload the current level to restart it
    }
}
