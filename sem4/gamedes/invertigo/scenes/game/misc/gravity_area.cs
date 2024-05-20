using Godot;
using System;

public partial class gravity_area : Area2D
{
    private main_character _mainCharacter;
    private Vector2 _gravityDirectionBeforeChange;

    public override void _Ready()
	{
        _mainCharacter = GetNode<main_character>("/root/Main/MainCharacter");
        Messanger.Instance.Connect(Messanger.SignalName.GravitySwitched, Callable.From(OnGravitySwitched));
    }

    public void OnBodyEntered(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            _gravityDirectionBeforeChange = -_mainCharacter.UpDirection;
            if (AreFloatsEqual(RotationDegrees, 90))
            {
                GD.Print("On Enter: Set gravity to normal");
                Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToNormal);
            }
            else
            {
                GD.Print("On Enter: Set gravity to inverted");
                Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToInverted);
            }
        }
    }

    public void OnBodyExited(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            GD.Print($"_gravityDirectionBeforeChange: {_gravityDirectionBeforeChange}");
            GD.Print($"RotationDegrees: {RotationDegrees}");
            if ((AreFloatsEqual(RotationDegrees, 90) && AreFloatsEqual(_gravityDirectionBeforeChange.Y, Vector2.Down.Y)) 
                || (AreFloatsEqual(RotationDegrees, -90) && AreFloatsEqual(_gravityDirectionBeforeChange.Y, Vector2.Down.Y)))
            {
                GD.Print("On Exit: Set gravity to normal");
                Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToNormal);
            }
            else
            {
                GD.Print("On Exit: Set gravity to inverted");
                Messanger.Instance.EmitSignal(Messanger.SignalName.GravitySetToInverted);
            }
        }
    }

    public void OnGravitySwitched()
    {
        _gravityDirectionBeforeChange = _gravityDirectionBeforeChange.Rotated(Mathf.Pi);
    }

    private static bool AreFloatsEqual(float a, float b, float tolerance = 0.01f)
    {
        return Math.Abs(a - b) < tolerance;
    }
}
