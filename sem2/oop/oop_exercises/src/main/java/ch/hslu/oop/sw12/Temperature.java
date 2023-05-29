package ch.hslu.oop.sw12;

public final class Temperature implements Comparable<Temperature> {
    public static final double KELVIN_OFFSET = 273.15;
    private final double temperatureInKelvin;

    private Temperature(final double temperatureInKelvin) {
        if (temperatureInKelvin < 0) {
            throw new IllegalArgumentException("Temperature in kelvin must be greater than 0");
        }

        this.temperatureInKelvin = temperatureInKelvin;
    }

    public static Temperature createFromKelvin(final double temperature) {
        return new Temperature(temperature);
    }

    public static Temperature createFromCelsius(final double temperature) {
        return new Temperature(convertCelsiusToKelvin(temperature));
    }

    public static double convertKelvinToCelsius(final double temperature) {
        return temperature - KELVIN_OFFSET;
    }

    public static double convertCelsiusToKelvin(final double temperature) {
        return temperature + KELVIN_OFFSET;
    }

    public double getTemperatureCelsius() {
        return convertKelvinToCelsius(this.temperatureInKelvin);
    }

    public double getTemperatureKelvin() {
        return this.temperatureInKelvin;
    }

    public double getTemperatureFahrenheit() {
        return (this.temperatureInKelvin * 9 / 5) - 459.67;
    }

    public Temperature changeTemperature(final double temperatureChangeInKelvin) {
        return Temperature.createFromKelvin(this.temperatureInKelvin + temperatureChangeInKelvin);
    }

    @Override
    public String toString() {
        return "Temperature [temperatureInKelvin=" + temperatureInKelvin + "]";
    }

    @Override
    public boolean equals(final Object object) {
        if (this == object) {
            return true;
        }

        return object instanceof Temperature t
                && Double.compare(this.temperatureInKelvin, t.temperatureInKelvin) == 0;
    }

    @Override
    public int hashCode() {
        return Double.hashCode(temperatureInKelvin);
    }

    @Override
    public int compareTo(final Temperature other) {
        return Double.compare(this.temperatureInKelvin, other.temperatureInKelvin);
    }
}