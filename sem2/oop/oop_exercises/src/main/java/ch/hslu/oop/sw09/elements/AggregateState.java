package ch.hslu.oop.sw09.elements;

public enum AggregateState {
    UNKNOWN,
    SOLID,
    LIQUID,
    GAS;

    public final String toString() {
        return this.name().toLowerCase();
    }
}
