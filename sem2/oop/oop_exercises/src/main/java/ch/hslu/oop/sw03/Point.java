package ch.hslu.oop.sw03;

public class Point {
    private int xCoordinate;
    private int yCoordinate;

    public Point(int xCoordinate, int yCoordinate) {
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

    public void setXCoordinate(int xCoordinate) {
        this.xCoordinate = xCoordinate;
    }

    public void setYCoordinate(int yCoordinate) {
        this.yCoordinate = yCoordinate;
    }
}