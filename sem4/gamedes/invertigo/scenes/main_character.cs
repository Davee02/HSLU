using Godot;
using System;

public partial class main_character : CharacterBody2D
{
	public const float Speed = 300.0f;
	public const float JumpVelocity = -400.0f;

	// Get the gravity from the project settings to be synced with RigidBody nodes.
	public float Gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();
	public bool IsGravityFlipped = false;

	private Sprite2D sprite2d;

	public override void _Ready()
	{
		sprite2d = GetNode<Sprite2D>("Sprite2D");
	}

    public override void _Process(double delta)
    {
        RotationDegrees = IsGravityFlipped ? 180 : 0;
    }

    public override void _PhysicsProcess(double delta)
	{
        UpDirection = IsGravityFlipped ? Vector2.Up.Rotated(Mathf.Pi) : Vector2.Up;
        Vector2 velocity = Velocity;
		var sign = IsGravityFlipped ? -1 : 1;

		// Add the gravity.
		if (!IsOnFloor())
			velocity.Y += sign * Gravity * (float)delta;

		// Handle Jump.
		if (Input.IsActionJustPressed("jump") && IsOnFloor())
			velocity.Y = sign * JumpVelocity;

		// Get the input direction and handle the movement/deceleration.
		// As good practice, you should replace UI actions with custom right actions.
		var direction = Input.GetAxis("left", "right");
		if (direction != 0)
		{
			velocity.X = direction * Speed;
		}
		else
		{
			velocity.X = Mathf.MoveToward(Velocity.X, 0, 100);
		}

		Velocity = velocity;
		MoveAndSlide();
	}
}
