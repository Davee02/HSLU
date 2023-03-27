package ch.hslu.oop.sw06.point;

public class Point {
    private int xCoordinate;
    private int yCoordinate;

    public Point(final int xCoordinate, final int yCoordinate) {
        this.xCoordinate = xCoordinate;
        this.yCoordinate = yCoordinate;
    }

    public Point(Point point) {
        this(point.getXCoordinate(), point.getYCoordinate());
    }

    public int getQuadrant() {
        if (xCoordinate > 0 && yCoordinate > 0) {
            return 1;
        } else if (xCoordinate < 0 && yCoordinate > 0) {
            return 2;
        } else if (xCoordinate < 0 && yCoordinate < 0) {
            return 3;
        } else if (xCoordinate > 0 && yCoordinate < 0) {
            return 4;
        } else {
            return 0;
        }
    }

    public void moveRelative(final int x, final int y) {
        this.xCoordinate += x;
        this.yCoordinate += y;
    }

    public void moveRelative(final Point point) {
        this.xCoordinate += point.getXCoordinate();
        this.yCoordinate += point.getYCoordinate();
    }

    public void moveRelative(final int amount, final double angle) {
        this.xCoordinate += amount * Math.cos(angle);
        this.yCoordinate += amount * Math.sin(angle);
    }

    public final int getXCoordinate() {
        return xCoordinate;
    }

    public final void setXCoordinate(final int xCoordinate) {
        this.xCoordinate = xCoordinate;
    }

    public final int getYCoordinate() {
        return yCoordinate;
    }

    public final void setYCoordinate(final int yCoordinate) {
        this.yCoordinate = yCoordinate;
    }
}