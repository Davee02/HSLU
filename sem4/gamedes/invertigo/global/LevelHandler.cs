using Godot;

public partial class LevelHandler : Node
{
    private int _currentLevel = 4;
    private Node _levelNode;
    private main_character _mainCharacter;

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.LevelCompleted, Callable.From(OnLevelCompleted));
        Messanger.Instance.Connect(Messanger.SignalName.CharacterDied, Callable.From(OnCharacterDied));

        _levelNode = GetNode("/root/Main/Level");
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

        var newLevel = ResourceLoader.Load<PackedScene>($"res://scenes/game/levels/level_{_currentLevel}.tscn");
        _levelNode.AddChild(newLevel.Instantiate());
        _mainCharacter.Position = new Vector2(100, 560);
        //Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySwitched);
    }

    private void OnCharacterDied()
    {
        GD.Print("Received character died signal");
        LoadLevel(); // reload the current level to restart it
    }
}
