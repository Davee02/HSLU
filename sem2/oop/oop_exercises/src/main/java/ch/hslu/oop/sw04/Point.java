package ch.hslu.oop.sw04;

public class Point {
    private int xCoordinate;
    private int yCoordinate;

    public Point(final int xCoordinate, final int yCoordinate) {
        this.xCoordinate = xCoordinate;
        this.yCoordinate = yCoordinate;
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