using Godot;

public partial class end_screen : Control
{
	private time_display _timeDisplay;
	private RichTextLabel _timeDisplayLabel;

    public override void _Ready()
	{
		Hide();
        Messanger.Instance.Connect(Messanger.SignalName.GameFinished, Callable.From(OnGameFinished));

        _timeDisplayLabel = GetNode<RichTextLabel>("TimeDisplayLabel");
        _timeDisplay = GetNode<time_display>("../TimeDisplay");
    }

	public void OnGameFinished()
	{
		GetTree().Paused = true;
        _timeDisplayLabel.Text = $"It took you {_timeDisplay.ElapsedTime.TotalSeconds} seconds";
        Show();
	}

	public void Quit()
    {
        GetTree().Quit();
    }

    public void RestartGame()
    {
        Messanger.Instance.EmitSignal(Messanger.SignalName.GameRestarted);
        Hide();
        GetTree().Paused = false;
    }
}
