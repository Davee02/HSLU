package ch.hslu.oop.sw11.car;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.beans.PropertyChangeEvent;

/**
 * This class represents a car. It is a composite of the engine and wipers.
 */
public class Car implements ICountingSwitchable, IHasName {

    private static final Logger LOG = LogManager.getLogger(Car.class);
    private final Engine engine;
    private final ISwitchable wipers;
    private boolean isSwitchedOn;
    private long switchCount;
    private String name;

    public Car() {
        engine = new Engine();
        wipers = new Wipers();

        engine.addChangeListener(this::onEnginePropertyChanged);
    }

    public void switchOn() {
        switchCount++;
        engine.switchOn();
        wipers.switchOn();
        isSwitchedOn = true;
    }

    public void switchOff() {
        switchCount++;
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

    @Override
    public long getSwitchCount() {
        return switchCount;
    }

    @Override
    public final String getName() {
        return this.name;
    }

    @Override
    public final void setName(final String name) {
        this.name = name;
    }

    private void onEnginePropertyChanged(final PropertyChangeEvent event) {
        LOG.info("Property changed: {} from {} to {}", event.getPropertyName(), event.getOldValue(), event.getNewValue());
    }
}
