package ch.hslu.oop.sw09.elements;

public final class Mercury extends Element {

    public Mercury() {
        super("Hg", -38.83, 356.73);
    }

    @Override
    public String toString() {
        return super.toString() + " - Poisonous";
    }
}
