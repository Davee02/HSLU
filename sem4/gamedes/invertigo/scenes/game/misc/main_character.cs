using Godot; 

public partial class main_character : CharacterBody2D
{
	private bool _isGravityFlipped = false;

	public const float Speed = 300.0f;
	public const float JumpVelocity = -400.0f;

	// Get the gravity from the project settings to be synced with RigidBody nodes.
	public float Gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();

	public override void _Ready()
	{
		Messanger.Instance.Connect(Messanger.SignalName.GravitySwitched, Callable.From(OnGravitySwitched));
	}

    public override void _PhysicsProcess(double delta)
	{
        Vector2 velocity = Velocity;
		var sign = _isGravityFlipped ? -1 : 1;

		// Add the gravity.
		if (!IsOnFloor())
			velocity.Y += sign * Gravity * (float)delta;

		// Handle Jump.
		if (Input.IsActionJustPressed("jump") && IsOnFloor())
			velocity.Y = sign * JumpVelocity;

		// Get the input direction and handle the movement/deceleration.
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

	public void OnGravitySwitched()
	{
        _isGravityFlipped = !_isGravityFlipped;
		RotationDegrees = _isGravityFlipped ? 180 : 0;
		UpDirection = _isGravityFlipped ? Vector2.Up.Rotated(Mathf.Pi) : Vector2.Up;
    }
}
