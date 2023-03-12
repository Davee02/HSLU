/**
 * Represents a line with a start point and an end point.
 */
public class Line {
    private Point startPoint;
    private Point endPoint;

    /**
     * Creates a line with the given start and end points.
     */
    public Line(int x1, int y1, int x2, int y2) {
        startPoint = new Point(x1, y1);
        endPoint = new Point(x2, y2);
    }

    public Point getStartPoint() {
        return startPoint;
    }

    public Point getEndPoint() {
        return endPoint;
    }

    public void setStartPoint(int x, int y) {
        startPoint.setXCoordinate(x);
        startPoint.setYCoordinate(y);
    }

    public void setEndPoint(int x, int y) {
        endPoint.setXCoordinate(x);
        endPoint.setYCoordinate(y);
    }
}
