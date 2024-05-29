using Godot;

public partial class movable_box : RigidBody2D
{
    private bool _isGravityFlipped = false;
    private bool _hasPlayedSoundForFlippedGravity = true;
    private double _timeSinceLastGravityFlip = 0;
    private float _previousAngle;
    private float _rotationAccumulator;
    private AudioStreamPlayer _rotationAudioPlayer;

    public override void _Ready()
    {
        Messanger.Instance.Connect(Messanger.SignalName.GravitySwitched, Callable.From(OnGravitySwitched));
        _rotationAudioPlayer = GetNode<AudioStreamPlayer>("BoxRotationAudioPlayer");

        _previousAngle = Rotation;
    }

    public override void _PhysicsProcess(double delta)
    {
        _timeSinceLastGravityFlip += delta;

        if (_timeSinceLastGravityFlip >= 0.5 && !_hasPlayedSoundForFlippedGravity && Mathf.Snapped(LinearVelocity.Y, 0.05f) == 0)
        {
            // play sound after gravity has been flipped and the box has stopped moving (= it has arrived at a new position)
            _hasPlayedSoundForFlippedGravity = true;
            _rotationAudioPlayer.Play();
        }

        var angleDifference = Rotation - _previousAngle;
        _previousAngle = Rotation;
        _rotationAccumulator += angleDifference;

        if (Mathf.Abs(_rotationAccumulator) >= Mathf.Pi / 2)
        {
            // play sound after the box has been rotated by 90 degrees
            _rotationAccumulator = 0;
            _rotationAudioPlayer.Play();
        }
    }

    public void OnGravitySwitched()
    {
        SetGravityFlipped(!_isGravityFlipped);
    }

    public void SetGravityFlipped(bool flipped)
    {
        _timeSinceLastGravityFlip = 0;
        _hasPlayedSoundForFlippedGravity = false;
        _isGravityFlipped = flipped;

        Sleeping = false;
        GravityScale = _isGravityFlipped ? -1 : 1;
    }
}
