package ch.hslu.oop.sw09;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;

public final class TemperatureHistory {
    private final Collection<Temperature> temperatures;

    public TemperatureHistory() {
        // this.temperatures = new HashSet<>();
        this.temperatures = new ArrayList<>();
    }

    public final void add(final Temperature temperature) {
        this.temperatures.add(temperature);
    }

    public final void clear() {
        this.temperatures.clear();
    }

    public final int getCount() {
        return this.temperatures.size();
    }

    public final boolean hasValues() {
        return this.getCount() > 0;
    }

    public final Temperature getMax() {
        return this.hasValues()
                ? Collections.max(this.temperatures)
                : new Temperature(0);
    }

    public final Temperature getMin() {
        return this.hasValues()
                ? Collections.min(this.temperatures)
                : new Temperature(0);
    }

    public final double getAverage() {
        if (!this.hasValues()) {
            return 0;
        }

        double sum = 0;
        for (Temperature temperature : this.temperatures) {
            sum += temperature.getTemperatureCelsius();
        }
        return sum / this.getCount();
    }
}
