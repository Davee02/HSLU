package ch.hslu.oop.sw04;

/**
 * Represents a line with a start point and an end point.
 */
public class Line {
    private Point startPoint;
    private Point endPoint;

    /**
     * Creates a line with the given start and end points.
     */
    public Line(final int x1, final int y1, final int x2, final int y2) {
        startPoint = new Point(x1, y1);
        endPoint = new Point(x2, y2);
    }

    public final Point getStartPoint() {
        return startPoint;
    }

    public final Point getEndPoint() {
        return endPoint;
    }

    public final void setStartPoint(final int x, final int y) {
        startPoint.setXCoordinate(x);
        startPoint.setYCoordinate(y);
    }

    public final void setEndPoint(final int x, final int y) {
        endPoint.setXCoordinate(x);
        endPoint.setYCoordinate(y);
    }
}
