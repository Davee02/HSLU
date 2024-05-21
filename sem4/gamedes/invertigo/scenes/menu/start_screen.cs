using Godot;

public partial class start_screen : Control
{
    public override void _Ready()
    {
        GetTree().Paused = true;
    }

    public override void _Process(double delta)
	{
		if (Input.IsAnythingPressed())
        {
            GetTree().Paused = false;
            Messanger.Instance.EmitSignal(Messanger.SignalName.GameStarted);
            Free();
        }
    }
}
