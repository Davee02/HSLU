package ch.hslu.oop.sw06.shapes;

public final class Circle extends Shape {
    private int diameter;

    public Circle(final int x, final int y, final int diameter) {
        super(x, y);
        this.diameter = diameter;
    }

    @Override
    public int getPerimeter() {
        return (int) (Math.PI * this.diameter);
    }

    @Override
    public int getArea() {
        return (int) (Math.PI * Math.pow(this.diameter / 2, 2));
    }

    public final void setDiameter(final int newDiameter) {
        this.diameter = newDiameter;
    }

    public final int getDiameter() {
        return this.diameter;
    }
}
