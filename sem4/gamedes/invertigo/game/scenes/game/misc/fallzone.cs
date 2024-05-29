using Godot;

public partial class fallzone : Area2D
{
    private AudioStreamPlayer _dieAudioPlayer;

    public override void _Ready()
    {
        _dieAudioPlayer = GetNode<AudioStreamPlayer>("DieAudioPlayer");
    }

    public void OnBodyEntered(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            GD.Print("Player has fallen to death");
            Messanger.Instance.EmitSignal(Messanger.SignalName.CharacterDied);
            _dieAudioPlayer.Play();
        }
        else
        {
            // remove any other body that falls into the fallzone
            body.QueueFree();
        }
    }
}
