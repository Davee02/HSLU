public class Element {
    private double meltingTemperatureCelsius;
    private double boilingTemperatureCelsius;
    private String elementCode;

    public Element(String elementCode, int meltingTemperatureCelsius, int boilingTemperatureCelsius) {
        this.elementCode = elementCode;
        this.meltingTemperatureCelsius = meltingTemperatureCelsius;
        this.boilingTemperatureCelsius = boilingTemperatureCelsius;
    }

    public double getMeltingTemperatureCelsius() {
        return this.meltingTemperatureCelsius;
    }

    public double getBoilingTemperatureCelsius() {
        return boilingTemperatureCelsius;
    }
}
