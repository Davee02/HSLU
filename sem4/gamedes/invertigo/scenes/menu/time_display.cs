using Godot;
using System;

public partial class time_display : RichTextLabel
{

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.GameRestarted, Callable.From(OnGameRestarted));
        Messanger.Instance.Connect(Messanger.SignalName.GameFinished, Callable.From(OnGameFinished));
    }

    public override void _Process(double delta)
	{
        Text = ElapsedTime.ToString(@"mm\:ss\:ff");
    }

	public TimeSpan ElapsedTime { get; private set; } = TimeSpan.Zero;

    public void OnTimerTimeout()
	{
        ElapsedTime = ElapsedTime.Add(TimeSpan.FromSeconds(0.1));
    }

    public void OnGameRestarted()
    {
        ElapsedTime = TimeSpan.Zero;
        Show();
    }

    public void OnGameFinished()
    {
        Hide();
    }
}
