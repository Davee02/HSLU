package ch.hslu.oop.sw05.shapes;

public final class Square extends Shape {
    private int width;

    public Square(final int x, final int y, final int width) {
        super(x, y);
        this.width = width;
    }

    @Override
    public int getPerimeter() {
        return 4 * this.width;
    }

    @Override
    public int getArea() {
        return this.width * this.width;
    }

    public final int getWidth() {
        return this.width;
    }

    public void changeDimensions(final int newWidth) {
        this.width = newWidth;
    }
}
