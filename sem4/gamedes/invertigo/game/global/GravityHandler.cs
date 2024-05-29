using Godot;

public partial class GravityHandler : Node
{
    private main_character _mainCharacter;
    private Vector2 _gravityDirectionBeforeChange;
    private bool _isGravityInverted = false;

    public override void _Ready()
    {
        _mainCharacter = GetNode<main_character>("/root/Main/Game/MainCharacter");
        Messanger.Instance.Connect(Messanger.SignalName.GravitySwitched, Callable.From(OnGravitySwitched));
        Messanger.Instance.Connect(Messanger.SignalName.GravitySetToNormal, Callable.From(OnGravitySetToNormal));
        Messanger.Instance.Connect(Messanger.SignalName.GravitySetToInverted, Callable.From(OnGravitySetToInverted));
    }

    public void OnGravitySwitched()
    {
        if (_isGravityInverted)
        {
            OnGravitySetToNormal();
        }
        else
        {
            OnGravitySetToInverted();
        }
    }

    public void OnGravitySetToNormal()
    {
        if (_isGravityInverted)
        {
            _isGravityInverted = false;
            SetGravityDirection(_mainCharacter.UpDirection.Rotated(Mathf.Pi));
        }
    }

    public void OnGravitySetToInverted()
    {
        if (!_isGravityInverted)
        {
            _isGravityInverted = true;
            SetGravityDirection(_mainCharacter.UpDirection.Rotated(Mathf.Pi));
        }
    }

    private void SetGravityDirection(Vector2 direction)
    {
        _mainCharacter.UpDirection = direction;
        _mainCharacter.Rotation = direction.AngleTo(Vector2.Up);
    }
}