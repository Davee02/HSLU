package ch.hslu.oop.sw06.elements;

public class Mercury extends Element {

    public Mercury() {
        super("Hg", -38.83, 356.73);
    }

    @Override
    public String toString() {
        return super.toString() + " - Poisonous";
    }
}
