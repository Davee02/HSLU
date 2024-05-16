using Godot;
using System;

public partial class gravity_area : Area2D
{
    private main_character _mainCharacter;
    private Vector2 _gravityDirectionBeforeChange;

    public override void _Ready()
	{
        _mainCharacter = GetNode<main_character>("/root/Main/MainCharacter");
    }

    public void OnBodyEntered(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            _gravityDirectionBeforeChange = _mainCharacter.UpDirection;
            _mainCharacter.SetGravityDirection(AreFloatsEqual(RotationDegrees, 90) ? Vector2.Up : Vector2.Down);
        }
    }

    public void OnBodyExited(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            _mainCharacter.SetGravityDirection(_gravityDirectionBeforeChange);
        }
    }

    private static bool AreFloatsEqual(float a, float b, float tolerance = 0.01f)
    {
        return Math.Abs(a - b) < tolerance;
    }
}
