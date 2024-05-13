using Godot;

public partial class main_character : CharacterBody2D
{
    private bool _isGravityFlipped = false;
    private AnimatedSprite2D _animatedSprite;

    public const float Speed = 300.0f;
    public const float JumpVelocity = -400.0f;
    public const float PushStrength = 40f;

    // Get the gravity from the project settings to be synced with RigidBody nodes.
    public float Gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.GravitySwitched, Callable.From(OnGravitySwitched));
        _animatedSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
    }

    public override void _PhysicsProcess(double delta)
    {
        Vector2 velocity = Velocity;
        var sign = _isGravityFlipped ? -1 : 1;

        // Set animation
        _animatedSprite.Animation = GetAnimationToPlay();


        // Add the gravity.
        if (!IsOnFloor())
        {
            velocity.Y += sign * Gravity * (float)delta;
  
        }

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

        HandleRigidBodyCollisions();
    }

    public void OnGravitySwitched()
    {
        SetGravityFlipped(!_isGravityFlipped);
    }

    public void SetGravityFlipped(bool flipped)
    {
        _isGravityFlipped = flipped;
        RotationDegrees = _isGravityFlipped ? 180 : 0;
        UpDirection = _isGravityFlipped ? Vector2.Up.Rotated(Mathf.Pi) : Vector2.Up;
    }

    private string GetAnimationToPlay()
    {
        return (Mathf.Abs(Velocity.X), IsOnFloor()) switch
        {
            (_, false) => "jumping",
            ( > 1, _) => "walking",
            (_, _) => "standing"
        };
    }

    private void HandleRigidBodyCollisions()
    {
        for (int i = 0; i < GetSlideCollisionCount(); i++)
        {
            var collision = GetSlideCollision(i);
            var collider = collision.GetCollider();
            if (collider is RigidBody2D rigidBody)
            {
                rigidBody.ApplyCentralImpulse(-collision.GetNormal() * PushStrength);
            }
        }
    }
}
