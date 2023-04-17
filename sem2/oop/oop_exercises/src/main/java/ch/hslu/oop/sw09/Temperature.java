package ch.hslu.oop.sw09;

import ch.hslu.oop.sw05.elements.AggregateState;
import ch.hslu.oop.sw05.elements.Element;

public final class Temperature implements Comparable<Temperature> {
    public static final double KELVIN_OFFSET = 273.15;
    private double earthTemperatureCelsius;

    public Temperature(double temperature) {
        this.earthTemperatureCelsius = temperature;
    }

    public Temperature() {
        this.earthTemperatureCelsius = 20;
    }

    public static double convertKelvinToCelsius(final double temperature) {
        return temperature - KELVIN_OFFSET;
    }

    public static double convertCelsiusToKelvin(final double temperature) {
        return temperature + KELVIN_OFFSET;
    }

    public double getTemperatureCelsius() {
        return this.earthTemperatureCelsius;
    }

    public void setTemperatureCelsius(float temperature) {
        this.earthTemperatureCelsius = temperature;
    }

    public double getTemperatureKelvin() {
        return convertCelsiusToKelvin(this.earthTemperatureCelsius);
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

        return object instanceof Temperature t
                && Double.compare(this.earthTemperatureCelsius, t.earthTemperatureCelsius) == 0;
    }

    @Override
    public final int hashCode() {
        return Double.hashCode(earthTemperatureCelsius);
    }

    @Override
    public final int compareTo(final Temperature other) {
        return Double.compare(this.earthTemperatureCelsius, other.earthTemperatureCelsius);
    }
}