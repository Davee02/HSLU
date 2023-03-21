package ch.hslu.oop.sw04;

/**
 * This class represents a car. It is a composite of the engine and wipers.
 */
public class Car implements ISwitchable {
    private ISwitchable engine;
    private ISwitchable wipers;
    private boolean isSwitchedOn;

    public Car() {
        Engine engine = new Engine();
        engine.setRotationsPerMinute(600);
        this.engine = engine;
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
        return isSwitchedOn;
    }

    public boolean isSwitchedOff() {
        return !isSwitchedOn;
    }
}
