using Godot;

public partial class next_level : Area2D
{
    public void OnBodyEntered(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            GD.Print("Completed a level");
            NextLevel();
        }
    }

    private void NextLevel()
    {
        Messanger.Instance.EmitSignal(Messanger.SignalName.LevelCompleted);
    }
}
