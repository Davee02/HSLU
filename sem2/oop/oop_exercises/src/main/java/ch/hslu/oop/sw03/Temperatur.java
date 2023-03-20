package ch.hslu.oop.sw03;

public class Temperatur {
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
}