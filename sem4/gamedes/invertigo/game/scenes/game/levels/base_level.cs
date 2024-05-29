using Godot;
using System;

public partial class base_level : Node2D
{
    [Export]
    public bool StartWithFlippedGravity { get; set; }

    [Export]
    public Vector2 CharacterStartPosition { get; set; }
}
