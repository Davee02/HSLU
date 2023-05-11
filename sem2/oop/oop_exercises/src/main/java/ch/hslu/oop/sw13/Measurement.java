package ch.hslu.oop.sw13;

import java.time.LocalDateTime;
import java.util.Objects;

public final class Measurement implements Comparable<Measurement> {
    private final Temperature temperature;
    private final LocalDateTime timestamp;

    public Measurement(Temperature temperature, LocalDateTime timestamp) {
        this.temperature = temperature;
        this.timestamp = timestamp;
    }

    public static Measurement Empty() {
        return new Measurement(Temperature.createFromCelsius(0), LocalDateTime.MIN);
    }

    public Temperature getTemperature() {
        return this.temperature;
    }

    public LocalDateTime getTimestamp() {
        return this.timestamp;
    }

    @Override
    public String toString() {
        return "Measurement [temperature=" + temperature + ", dateTime=" + timestamp + "]";
    }

    @Override
    public boolean equals(final Object object) {
        if (this == object) {
            return true;
        }

        return object instanceof Measurement m
                && this.temperature.equals(m.temperature)
                && this.timestamp.equals(m.timestamp);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.temperature, this.timestamp);
    }

    @Override
    public int compareTo(Measurement measurement) {
        return this.temperature.compareTo(measurement.temperature);
    }
}
