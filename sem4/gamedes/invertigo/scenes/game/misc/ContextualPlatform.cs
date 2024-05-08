using Godot;

public partial class ContextualPlatform : Node2D
{
    private bool _isGravityFlipped = false;
    private StaticBody2D _staticBody;

    [Export]
	public bool WorkOnlyInFlippedGravity { get; set; }


    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
	{
        Messanger.Instance.Connect(Messanger.SignalName.GravitySwitched, Callable.From(OnGravitySwitched));
        _staticBody = GetNode<StaticBody2D>("StaticBody2D");
        SetCollisionBasedOnGravity();
    }

    public void OnGravitySwitched()
    {
        _isGravityFlipped = !_isGravityFlipped;
        SetCollisionBasedOnGravity();
    }

    private void SetCollisionBasedOnGravity()
    {
        bool enableCollision = WorkOnlyInFlippedGravity == _isGravityFlipped;
        GD.Print($"Collision enabled: {enableCollision}");

        _staticBody.SetCollisionMaskValue(1, enableCollision);
        _staticBody.SetCollisionLayerValue(1, enableCollision);

    }
}
