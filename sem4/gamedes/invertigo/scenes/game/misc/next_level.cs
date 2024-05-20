using Godot;

public partial class next_level : Area2D
{
    private AudioStreamPlayer _finishLevelAudioPlayer;

    public override void _Ready()
    {
        _finishLevelAudioPlayer = GetNode<AudioStreamPlayer>("FinishLevelAudioPlayer");
    }

    public void OnBodyEntered(Node body)
    {
        if (body.IsInGroup("MainCharacter"))
        {
            GD.Print("Completed a level");
            _finishLevelAudioPlayer.Play();
            Messanger.Instance.EmitSignal(Messanger.SignalName.LevelCompleted);
        }
    }
}
