package ch.hslu.oop.sw06.elements;

public abstract class Element {
    private double meltingTemperatureCelsius;
    private double boilingTemperatureCelsius;
    private String elementCode;

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

    @Override
    public String toString() {
        return "Element [meltingTemperatureCelsius=" + meltingTemperatureCelsius + ", boilingTemperatureCelsius="
                + boilingTemperatureCelsius + ", elementCode=" + elementCode + "]";
    }
}
