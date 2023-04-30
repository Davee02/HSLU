package ch.hslu.oop.sw11.car;

/**
 * Interface for devices that can be switched on and off and that keep track of
 * the number of times they have been switched on.
 */
public interface ICountingSwitchable extends ISwitchable {
    /**
     * Returns the number of times the device has been switched on.
     */
    long getSwitchCount();
}
