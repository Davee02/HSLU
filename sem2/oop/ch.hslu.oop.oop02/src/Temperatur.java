public class Temperatur {
    private double temperaturInCelsius;

    public Temperatur() {
        this.temperaturInCelsius = 20;
    }

    public Temperatur(double temperaturInCelsius) {
        this.temperaturInCelsius = temperaturInCelsius;
    }

    public double getTemperaturInCelsius() {
        return temperaturInCelsius;
    }

    public void setTemperaturInCelsius(double temperaturInCelsius) {
        this.temperaturInCelsius = temperaturInCelsius;
    }

    public double getTemperaturInKelvin() {
        return temperaturInCelsius + 27.15;
    }

    public double getTemperaturInFahrenheit() {
        return temperaturInCelsius * 1.8 + 32;
    }

    public void changeTemperaturCelsius(double temperaturInCelsius) {
        this.temperaturInCelsius += temperaturInCelsius;
    }

    public void changeTemperaturKelvin(double temperaturInKelvin) {
        double celsius = temperaturInKelvin - 27.15;
        this.temperaturInCelsius += celsius;
    }
}
