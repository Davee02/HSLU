package ch.hslu.oop.sw11.temperature;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public final class TemperatureHistory {
    private final Collection<Temperature> temperatures;
    private final List<ITemperatureExtremeListener> temperatureExtremeListeners = new ArrayList<>();

    public TemperatureHistory() {
        this.temperatures = new ArrayList<>();
    }

    public void add(final Temperature temperature) {
        this.temperatures.add(temperature);

        if (getCount() > 1 && getMax() == temperature) {
            this.notifyExtremeTempListeners(ExtremeTypes.MAXIMUM, temperature);
        } else if (getCount() > 1 && getMin() == temperature) {
            this.notifyExtremeTempListeners(ExtremeTypes.MINIMUM, temperature);
        }
    }

    public void clear() {
        this.temperatures.clear();
    }

    public int getCount() {
        return this.temperatures.size();
    }

    public boolean hasValues() {
        return this.getCount() > 0;
    }

    public Temperature getMax() {
        return this.hasValues()
                ? Collections.max(this.temperatures)
                : Temperature.createFromCelsius(0);
    }

    public Temperature getMin() {
        return this.hasValues()
                ? Collections.min(this.temperatures)
                : Temperature.createFromCelsius(0);
    }

    public double getAverage() {
        if (!this.hasValues()) {
            return 0;
        }

        double sum = 0;
        for (Temperature temperature : this.temperatures) {
            sum += temperature.getTemperatureCelsius();
        }
        return sum / this.getCount();
    }

    public void addTemperatureExtremeListener(final ITemperatureExtremeListener listener) {
        if (listener == null) {
            throw new IllegalArgumentException("listener must not be null");
        }

        this.temperatureExtremeListeners.add(listener);
    }

    public void removeTemperatureExtremeListener(final ITemperatureExtremeListener listener) {
        if (listener == null) {
            throw new IllegalArgumentException("listener must not be null");
        }

        this.temperatureExtremeListeners.remove(listener);
    }

    private void notifyExtremeTempListeners(final ExtremeTypes extremeType, final Temperature temperature) {
        for (ITemperatureExtremeListener listener : this.temperatureExtremeListeners) {
            listener.extremeTemperatureReached(new TemperatureExtremeEvent(this, extremeType, Temperature.createFromKelvin(temperature.getTemperatureKelvin())));
        }
    }
}
