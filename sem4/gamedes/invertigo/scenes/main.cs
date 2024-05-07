using Godot;

public partial class main : Node
{
	private int _currentLevel = 1;

	public override void _Ready()
	{
        Messanger.Instance.Connect(Messanger.SignalName.LevelCompleted, Callable.From(OnLevelCompleted));
    }

	public void OnLevelCompleted()
	{
        GD.Print("Received level completed signal");
        _currentLevel++;
        LoadLevel();
    }

    private void LoadLevel()
    {
        var level = $"res://scenes/game/levels/level_{_currentLevel}.tscn";
        GetTree().ChangeSceneToFile(level);
    }
}
