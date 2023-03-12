/**
 * Interface for devices that can be switched on and off.
 */
public interface ISwitchable {
    /**
     * Switches the device on.
     */
    void switchOn();

    /**
     * Switches the device off.
     */
    void switchOff();

    /**
     * Returns true if the device is switched on.
     */
    boolean isSwitchedOn();

    /**
     * Returns true if the device is switched off.
     */
    boolean isSwitchedOff();
}
