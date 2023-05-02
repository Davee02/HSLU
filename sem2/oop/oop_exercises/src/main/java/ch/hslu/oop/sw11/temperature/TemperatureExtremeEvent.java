package ch.hslu.oop.sw11.temperature;

import java.util.EventObject;

public final class TemperatureExtremeEvent extends EventObject {
    private static final long serialVersionUID = 1L;
    private final ExtremeTypes extremeType;
    private final Temperature temperature;

    public TemperatureExtremeEvent(Object source, ExtremeTypes extremeType, Temperature temperature) {
        super(source);
        this.extremeType = extremeType;
        this.temperature = temperature;
    }

    public ExtremeTypes getExtremeType() {
        return this.extremeType;
    }

    public Temperature getTemperature() {
        return this.temperature;
    }

    @Override
    public String toString() {
        return "TemperatureExtremeEvent [extremeType=" + extremeType + ", temperature=" + temperature + "]";
    }
}
