package ch.hslu.oop.sw05.shapes;

public final class Rectangle extends Shape {
    private int width;
    private int height;
    public Rectangle(final int x, final int y,
                     final int width, final int height) {
        super(x, y);
        this.width = width;
        this.height = height;
    }

    @Override
    public int getPerimeter() {
        return (2 * this.width) + (2 * this.height);
    }

    @Override
    public int getArea() {
        return this.width * this.height;
    }

    public int getWidth() {
        return this.width;
    }

    public int getHeight() {
        return this.height;
    }

    public void changeDimensions(final int newWidth, final int newHeight) {
        this.width = newWidth;
        this.height = newHeight;
    }
}
