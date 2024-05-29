using Godot;

public partial class pause_menu : Control
{
    private AnimationPlayer _animationPlayer;
    private bool _isGameFinished;

	public override void _Ready()
	{
        Hide();
        _animationPlayer = GetNode<AnimationPlayer>("AnimationPlayer");
        _animationPlayer.Play("RESET");

        Messanger.Instance.Connect(Messanger.SignalName.GameFinished, Callable.From(OnGameFinished));
        Messanger.Instance.Connect(Messanger.SignalName.GameRestarted, Callable.From(OnGameRestarted));
    }

    public override void _Process(double delta)
    {
        TestEsc();
    }

    public void Resume()
	{
        GD.Print("Resuming game");

        _animationPlayer.PlayBackwards("blur");
        Hide();
        GetTree().Paused = false;
    }

    public void Pause()
    {
        GD.Print("Pausing game");

        Show();
        _animationPlayer.Play("blur");
        GetTree().Paused = true;
    }

    public void RestartLevel()
    {
        GD.Print("Restarting level");

        Messanger.Instance.EmitSignal(Messanger.SignalName.CharacterDied);
        Resume();
    }

    public void RestartGame()
    {
        GD.Print("Restarting game");

        Messanger.Instance.EmitSignal(Messanger.SignalName.GameRestarted);
        Resume();
    }

    public void Quit()
    {
        GD.Print("Quitting game");

        GetTree().Quit();
    }

    public void TestEsc()
	{
		if (!_isGameFinished && Input.IsActionJustPressed("esc"))
		{
            if (GetTree().Paused)
			{
                Resume();
            }
            else
			{
                Pause();
            }
        }
	}

    public void OnGameFinished()
    {
        _isGameFinished = true;
    }

    public void OnGameRestarted()
    {
        _isGameFinished = false;
    }
}
