using Godot;

public partial class gravity_switcher : Area2D
{
	private bool _isReachable = false;
    private AudioStreamPlayer _gravitySwitchSoundPlayer;

    public override void _Ready()
    {
        _gravitySwitchSoundPlayer = GetNode<AudioStreamPlayer>("GravitySwitchAudioPlayer");
    }

    public override void _Process(double delta)
	{
		if (_isReachable && Input.IsActionJustPressed("interact"))
		{
            Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySwitched);
            _gravitySwitchSoundPlayer.Play();
        }
	}

	public void OnBodyEntered(Node body)
	{
        if (body.IsInGroup("MainCharacter"))
		{
            _isReachable = true;
        }
    }

    public void OnBodyExited(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            _isReachable = false;
        }
    }
}
