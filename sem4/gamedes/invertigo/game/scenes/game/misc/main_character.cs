using Godot;

public partial class main_character : CharacterBody2D
{
    private AnimatedSprite2D _animatedSprite;
    private AudioStreamPlayer _jumpAudioPlayer;
    private Timer _coyoteTimer;

    public const float Speed = 300.0f;
    public const float JumpVelocity = -400.0f;
    public const float PushStrength = 40f;

    // Get the gravity from the project settings to be synced with RigidBody nodes.
    public float Gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();

    public override void _Ready()
    {
        _animatedSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
        _jumpAudioPlayer = GetNode<AudioStreamPlayer>("JumpAudioPlayer");
        _coyoteTimer = GetNode<Timer>("CoyoteTimer");
    }

    public override void _PhysicsProcess(double delta)
    {
        Vector2 velocity = Velocity;
        Vector2 gravityDirection = -UpDirection;

        // Set animation
        _animatedSprite.Animation = GetAnimationToPlay();

        // Add the gravity.
        if (!IsOnFloor())
        {
            // calculate y velocity with gravity and gravity direction
            velocity.Y += (float)(Gravity * gravityDirection.Y * delta);
        }

        // Handle Jump.
        if (Input.IsActionJustPressed("jump") && (IsOnFloor() || !_coyoteTimer.IsStopped()))
        {
            velocity.Y = gravityDirection.Y * JumpVelocity;
            _jumpAudioPlayer.Play();
        }

        // Get the input direction and handle the movement/deceleration.
        var direction = Input.GetAxis("left", "right");
        if (direction != 0)
        {
            velocity.X = direction * Speed;
        }
        else
        {
            velocity.X = 0;
        }

        Velocity = velocity;

        var wasOnFLoor = IsOnFloor();
        MoveAndSlide();
        HandleRigidBodyCollisions();

        if (wasOnFLoor && !IsOnFloor() && !Input.IsActionJustPressed("jump"))
        {
            // start the coyote timer if the player was on the floor before moving and is not on the floor now
            _coyoteTimer.Start();
        }
    }

    private string GetAnimationToPlay()
    {
        return (Mathf.Abs(Velocity.X), IsOnFloor()) switch
        {
            ( > 1, true) => "walking",
            (_, false) => "jumping",
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
