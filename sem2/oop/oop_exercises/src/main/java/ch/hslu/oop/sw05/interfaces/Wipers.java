package ch.hslu.oop.sw05.interfaces;

/**
 * This class implements the ISwitchable interface for wipers and provides the
 * implementation for the methods defined in the interface.
 */
public class Wipers implements ICountingSwitchable, IHasName {
    private boolean areWiping;
    private long switchCount;
    private String name;

    @Override
    public void switchOn() {
        switchCount++;
        areWiping = true;
    }

    @Override
    public void switchOff() {
        switchCount++;
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
