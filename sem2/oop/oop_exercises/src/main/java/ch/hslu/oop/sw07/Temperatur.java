package ch.hslu.oop.sw07;

import ch.hslu.oop.sw07.elements.AggregateState;
import ch.hslu.oop.sw07.elements.Element;

public class Temperatur implements Comparable<Temperatur> {
    private double earthTemperatureCelsius;

    public Temperatur(double temperature) {
        this.earthTemperatureCelsius = temperature;
    }

    public Temperatur() {
        this.earthTemperatureCelsius = 20;
    }

    public double getTemperatureCelsius() {
        return this.earthTemperatureCelsius;
    }

    public void setTemperatureCelsius(float temperature) {
        this.earthTemperatureCelsius = temperature;
    }

    public double getTemperatureKelvin() {
        return this.earthTemperatureCelsius + 273.15;
    }

    public double getTemperatureFahrenheit() {
        return this.earthTemperatureCelsius * 1.8 + 32;
    }

    public void changeTemperature(double temperatureChangeInKelvin) {
        this.earthTemperatureCelsius = this.earthTemperatureCelsius + temperatureChangeInKelvin;
    }

    public AggregateState getAggregateState(Element element) {
        if (this.earthTemperatureCelsius <= element.getMeltingTemperatureCelsius()) {
            return AggregateState.SOLID;
        } else if (this.earthTemperatureCelsius >= element.getBoilingTemperatureCelsius()) {
            return AggregateState.GAS;
        } else {
            return AggregateState.LIQUID;
        }
    }

    @Override
    public String toString() {
        return "Temperatur [earthTemperatureCelsius=" + earthTemperatureCelsius + "]";
    }

    @Override
    public final boolean equals(final Object object) {
        if (this == object) {
            return true;
        }

        return object instanceof Temperatur t
                && Double.compare(this.earthTemperatureCelsius, t.earthTemperatureCelsius) == 0;
    }

    @Override
    public final int hashCode() {
        return Double.hashCode(earthTemperatureCelsius);
    }

    @Override
    public final int compareTo(final Temperatur other) {
        return Double.compare(this.earthTemperatureCelsius, other.earthTemperatureCelsius);
    }
}