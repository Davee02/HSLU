using Godot;
using System;

public partial class gravity_switcher : Area2D
{
	private bool _isReachable = false;
    private main_character _character;

    // Called every frame. 'delta' is the elapsed time since the previous frame.
    public override void _Process(double delta)
	{
		if (_isReachable && Input.IsActionJustPressed("interact"))
		{
            Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySwitched);
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
