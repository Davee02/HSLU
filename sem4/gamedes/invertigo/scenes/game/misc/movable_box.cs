using Godot;

public partial class movable_box : RigidBody2D
{
    private bool _isGravityFlipped = false;

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.GravitySwitched, Callable.From(OnGravitySwitched));
    }

    public void OnGravitySwitched()
    {
        SetGravityFlipped(!_isGravityFlipped);
    }

    public void SetGravityFlipped(bool flipped)
    {
        _isGravityFlipped = flipped;

        Sleeping = false;
        GravityScale = _isGravityFlipped ? -1 : 1;
    }
}
