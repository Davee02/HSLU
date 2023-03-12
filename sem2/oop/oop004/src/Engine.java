/**
 * This class implements the ISwitchable interface for an engine and provides the
 * implementation for the methods defined in the interface.
 */
public class Engine implements ISwitchable {
    private int rotationsPerMinute;

    @Override
    public void switchOn() {
        rotationsPerMinute = 600;
    }

    @Override
    public void switchOff() {
        rotationsPerMinute = 0;
    }

    @Override
    public boolean isSwitchedOn() {
        return rotationsPerMinute > 0;
    }

    @Override
    public boolean isSwitchedOff() {
        return rotationsPerMinute == 0;
    }

    public int getRotationsPerMinute() {
        return rotationsPerMinute;
    }

    public void setRotationsPerMinute(int rotationsPerMinute) {
        if (rotationsPerMinute < 0) {
            throw new IllegalArgumentException("Rotations per minute must be positive.");
        }

        this.rotationsPerMinute = rotationsPerMinute;
    }
}
