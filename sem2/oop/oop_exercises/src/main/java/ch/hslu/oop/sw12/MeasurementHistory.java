package ch.hslu.oop.sw12;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public final class MeasurementHistory {
    private final Collection<Measurement> measurements;
    private final List<IMeasurementExtremeListener> measurementExtremeListeners = new ArrayList<>();

    public MeasurementHistory() {
        this.measurements = new ArrayList<>();
    }

    public void add(final Measurement measurement) {
        this.measurements.add(measurement);

        if (getCount() > 1 && getMax() == measurement) {
            this.notifyExtremeMeasurementListeners(ExtremeTypes.MAXIMUM, measurement);
        } else if (getCount() > 1 && getMin() == measurement) {
            this.notifyExtremeMeasurementListeners(ExtremeTypes.MINIMUM, measurement);
        }
    }

    public void clear() {
        this.measurements.clear();
    }

    public int getCount() {
        return this.measurements.size();
    }

    public boolean hasValues() {
        return this.getCount() > 0;
    }

    public Measurement getMax() {
        return this.hasValues()
                ? Collections.max(this.measurements)
                : new Measurement(Temperature.createFromCelsius(0), LocalDateTime.MIN);
    }

    public Measurement getMin() {
        return this.hasValues()
                ? Collections.min(this.measurements)
                : new Measurement(Temperature.createFromCelsius(0), LocalDateTime.MIN);
    }

    public double getAverage() {
        if (!this.hasValues()) {
            return 0;
        }

        double sum = 0;
        for (Measurement measurement : this.measurements) {
            sum += measurement.getTemperature().getTemperatureCelsius();
        }
        return sum / this.getCount();
    }

    public void addMeasurementExtremeListener(final IMeasurementExtremeListener listener) {
        if (listener == null) {
            throw new IllegalArgumentException("listener must not be null");
        }

        this.measurementExtremeListeners.add(listener);
    }

    public void removeMeasurementExtremeListener(final IMeasurementExtremeListener listener) {
        if (listener == null) {
            throw new IllegalArgumentException("listener must not be null");
        }

        this.measurementExtremeListeners.remove(listener);
    }

    private void notifyExtremeMeasurementListeners(final ExtremeTypes extremeType, final Measurement measurement) {
        for (IMeasurementExtremeListener listener : this.measurementExtremeListeners) {
            listener.extremeMeasurementReached(new MeasurementExtremeEvent(this, extremeType, measurement));
        }
    }
}
