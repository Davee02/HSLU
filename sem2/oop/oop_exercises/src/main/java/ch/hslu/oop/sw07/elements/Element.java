package ch.hslu.oop.sw07.elements;

import java.util.Objects;

public abstract class Element implements Comparable<Element> {
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

    @Override
    public String toString() {
        return "Element [boilingTemperatureCelsius=" + boilingTemperatureCelsius + ", elementCode=" + elementCode
                + ", meltingTemperatureCelsius=" + meltingTemperatureCelsius + "]";
    }

    @Override
    public final boolean equals(final Object object) {
        if (this == object) {
            return true;
        }

        if (this.getClass() != this.getClass()) {
            return false;
        }

        return object instanceof Element e
                && Objects.equals(this.elementCode, e.elementCode)
                && Double.compare(this.meltingTemperatureCelsius, e.meltingTemperatureCelsius) == 0
                && Double.compare(this.boilingTemperatureCelsius, e.boilingTemperatureCelsius) == 0;
    }

    @Override
    public final int hashCode() {
        return Objects.hash(this.elementCode, this.meltingTemperatureCelsius, this.boilingTemperatureCelsius);
    }

    @Override
    public final int compareTo(final Element other) {
        return this.elementCode.compareTo(other.elementCode);
    }
}
