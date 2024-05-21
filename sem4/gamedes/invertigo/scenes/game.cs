using Godot;

public partial class game : Node2D
{
	public override void _Ready()
	{
        Messanger.Instance.Connect(Messanger.SignalName.GameStarted, Callable.From(OnGameStarted));
    }

    public void OnGameStarted()
    {
        Show();
    }
}
