using Godot;
using System;

public partial class gravity_switcher : Area2D
{
	private bool _isReachable = false;
    private main_character _character;

    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
	{
        _character = GetNode<CharacterBody2D>("%Character") as main_character;
    }

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		if (_isReachable && Input.IsActionJustPressed("interact"))
		{
            _character.IsGravityFlipped = !_character.IsGravityFlipped;
        }
	}

	public void OnBodyEntered(Node body)
	{
        if (body is main_character)
		{
            _isReachable = true;
        }
    }

    public void OnBodyExited(Node body)
    {
        if (body is main_character)
        {
            _isReachable = false;
        }
    }
}
