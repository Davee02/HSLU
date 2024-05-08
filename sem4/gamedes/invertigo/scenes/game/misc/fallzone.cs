using Godot;

public partial class fallzone : Area2D
{
    public void OnBodyEntered(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            GD.Print("Player has fallen to death");
            Messanger.Instance.EmitSignal(Messanger.SignalName.CharacterDied);
        }
    }
}
