package ch.hslu.oop.sw13;

import java.util.EventObject;

public final class MeasurementExtremeEvent extends EventObject {
    private static final long serialVersionUID = 1L;
    private final ExtremeTypes extremeType;
    private final Measurement measurement;

    public MeasurementExtremeEvent(Object source, ExtremeTypes extremeType, Measurement measurement) {
        super(source);
        this.extremeType = extremeType;
        this.measurement = measurement;
    }

    public ExtremeTypes getExtremeType() {
        return this.extremeType;
    }

    public Measurement getMeasurement() {
        return this.measurement;
    }

    @Override
    public String toString() {
        return "MeasurementExtremeEvent [extremeType=" + extremeType + ", measurement=" + measurement + "]";
    }
}
