package ch.hslu.oop.sw05.interfaces;

/**
 * This class represents a car. It is a composite of the engine and wipers.
 */
public class Car implements ICountingSwitchable, IHasName {
    private ISwitchable engine;
    private ISwitchable wipers;
    private boolean isSwitchedOn;
    private long switchCount;
    private String name;

    public Car() {
        engine = new Engine();
        wipers = new Wipers();
    }

    public void switchOn() {
        engine.switchOn();
        wipers.switchOn();
        isSwitchedOn = true;
    }

    public void switchOff() {
        engine.switchOff();
        wipers.switchOff();
        isSwitchedOn = false;
    }

    public boolean isSwitchedOn() {
        switchCount++;
        return isSwitchedOn;
    }

    public boolean isSwitchedOff() {
        switchCount++;
        return !isSwitchedOn;
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
