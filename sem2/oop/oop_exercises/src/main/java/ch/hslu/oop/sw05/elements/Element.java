package ch.hslu.oop.sw05.elements;

public abstract class Element {
    private final double meltingTemperatureCelsius;
    private final double boilingTemperatureCelsius;
    private final String elementCode;

    public Element(final String elementCode, final double meltingTemperatureCelsius, final double boilingTemperatureCelsius) {
        this.elementCode = elementCode;
        this.meltingTemperatureCelsius = meltingTemperatureCelsius;
        this.boilingTemperatureCelsius = boilingTemperatureCelsius;
    }

    public final double getMeltingTemperatureCelsius() {
        return this.meltingTemperatureCelsius;
    }

    public final double getBoilingTemperatureCelsius() {
        return boilingTemperatureCelsius;
    }

    public final String getElementCode() {
        return elementCode;
    }
}
