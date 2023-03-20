package ch.hslu.oop.sw05.interfaces;

/**
 * This class implements the ISwitchable interface for an engine and provides the
 * implementation for the methods defined in the interface.
 */
public class Engine implements ICountingSwitchable, IHasName {
    private int rotationsPerMinute;
    private long switchCount;
    private String name;

    @Override
    public void switchOn() {
        switchCount++;
        rotationsPerMinute = 600;
    }

    @Override
    public void switchOff() {
        switchCount++;
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

    public final int getRotationsPerMinute() {
        return rotationsPerMinute;
    }

    public final void setRotationsPerMinute(final int rotationsPerMinute) {
        if (rotationsPerMinute < 0) {
            throw new IllegalArgumentException("Rotations per minute must be positive.");
        }

        this.rotationsPerMinute = rotationsPerMinute;
    }

    @Override
    public long getSwitchCount() {
        return switchCount;
    }

    @Override
    public final String getName() {
        return null;
    }

    @Override
    public final String setName(final String name) {
        return this.name;
    }
}
