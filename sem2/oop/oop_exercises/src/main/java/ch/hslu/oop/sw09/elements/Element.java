package ch.hslu.oop.sw09.elements;

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

    public final String getAggregateState (final double temperatureCelsius) {
        if (temperatureCelsius < this.meltingTemperatureCelsius) {
            return getFormattedAggregateStateString(AggregateState.SOLID, temperatureCelsius);
        } else if (temperatureCelsius < this.boilingTemperatureCelsius) {
            return getFormattedAggregateStateString(AggregateState.LIQUID, temperatureCelsius);
        } else {
            return getFormattedAggregateStateString(AggregateState.GAS, temperatureCelsius);
        }
    }

    private final String getFormattedAggregateStateString(final AggregateState aggregateState, final double temperatureCelsius) {
        return String.format("%s has the aggregate state %s at %.2f°C", this.elementCode, aggregateState, temperatureCelsius);
    }

    @Override
    public String toString() {
        return "Element [meltingTemperatureCelsius=" + meltingTemperatureCelsius + ", boilingTemperatureCelsius="
                + boilingTemperatureCelsius + ", elementCode=" + elementCode + "]";
    }
}
