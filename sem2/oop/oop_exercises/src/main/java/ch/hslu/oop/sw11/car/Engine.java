package ch.hslu.oop.sw11.car;

import java.beans.PropertyChangeListener;
import java.util.ArrayList;
import java.util.List;

/**
 * This class implements the ISwitchable interface for an engine and provides the
 * implementation for the methods defined in the interface.
 */
public class Engine implements ICountingSwitchable, IHasName {
    private int rotationsPerMinute;
    private long switchCount;
    private String name;
    private final List<PropertyChangeListener> changeListeners = new ArrayList<>();

    @Override
    public void switchOn() {
        switchCount++;
        rotationsPerMinute = 600;
        firePropertyChangeEvent("rotationsPerMinute", 0, rotationsPerMinute);
    }

    @Override
    public void switchOff() {
        switchCount++;
        rotationsPerMinute = 0;
        firePropertyChangeEvent("rotationsPerMinute", 600, rotationsPerMinute);
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

        firePropertyChangeEvent("rotationsPerMinute", this.rotationsPerMinute, rotationsPerMinute);
        this.rotationsPerMinute = rotationsPerMinute;
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

    public final void addChangeListener(final PropertyChangeListener listener) {
        if (listener == null) {
            throw new IllegalArgumentException("Listener must not be null.");
        }

        changeListeners.add(listener);
    }

    public final void removeChangeListener(final PropertyChangeListener listener) {
        if (listener == null) {
            throw new IllegalArgumentException("Listener must not be null.");
        }

        changeListeners.remove(listener);
    }

    private void firePropertyChangeEvent(final String propertyName, final Object oldValue, final Object newValue) {
        for (PropertyChangeListener listener : changeListeners) {
            listener.propertyChange(new java.beans.PropertyChangeEvent(this, propertyName, oldValue, newValue));
        }
    }
}
