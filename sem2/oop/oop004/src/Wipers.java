/**
 * This class implements the ISwitchable interface for wipers and provides the
 * implementation for the methods defined in the interface.
 */
public class Wipers implements ISwitchable {
    private boolean areWiping;

    @Override
    public void switchOn() {
        areWiping = true;
    }

    @Override
    public void switchOff() {
        areWiping = false;
    }

    @Override
    public boolean isSwitchedOn() {
        return areWiping;
    }

    @Override
    public boolean isSwitchedOff() {
        return !areWiping;
    }
}
