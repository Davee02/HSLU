package ch.hslu.oop.sw05.interfaces;

/**
 * Interface for devices that have a name.
 */
public interface IHasName {
    /**
     * Returns the name of the device.
     */
    String getName();

    /**
     * Sets the name of the device.
     */
    String setName(final String name);
}
