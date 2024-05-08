using Godot;

public partial class MainCharacterCamera : Camera2D
{
    private main_character _mainCharacter;

    public override void _Ready()
	{
        _mainCharacter = GetNode<main_character>("/root/Main/MainCharacter");
    }

    public override void _PhysicsProcess(double delta)
    {
        Position = _mainCharacter.Position;
    }
}
