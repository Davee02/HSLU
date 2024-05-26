using Godot;

public partial class start_screen : Control
{
    private Control _controlsNode;
    private Control _storyNode;
    private int _clickCount = 0;
    private double _timeSinceLastClick = 0;

    public override void _Ready()
    {
        _controlsNode = GetNode<Control>("Controls");
        _storyNode = GetNode<Control>("Story");

        _storyNode.Visible = false;
        GetTree().Paused = true;
    }

    public override void _Process(double delta)
	{
        _timeSinceLastClick += delta;

        if (Input.IsAnythingPressed() && _timeSinceLastClick >= 0.2)
        {
            _clickCount++;
            _timeSinceLastClick = 0;

            if (_clickCount == 1)
            {
                _storyNode.Visible = true;
                _controlsNode.Visible = false;

            }
            else
            {
                GetTree().Paused = false;
                Messanger.Instance.EmitSignal(Messanger.SignalName.GameStarted);
                Free();
            }
        }
    }
}
