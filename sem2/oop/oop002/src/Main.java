public class Main {
    public static void main(String[] args) {
        Element pb = new Element("Pb", 327, 1740);
        Element n = new Element("N", -210, -196);
        Element hg = new Element("Hg", -39, 357);

        Temperatur t = new Temperatur(100);
        AggregateState pbAggregateState = t.getAggregateState(pb);
        AggregateState nAggregateState = t.getAggregateState(n);
        AggregateState hgAggregateState = t.getAggregateState(hg);

        System.out.println("Pb: " + pbAggregateState);
        System.out.println("N: " + nAggregateState);
        System.out.println("Hg: " + hgAggregateState);

        Point p1 = new Point(1, 1);
        System.out.println("Quadrant: " + p1.getQuadrant());

        p1.setXCoordinate(-1);
        System.out.println("Quadrant: " + p1.getQuadrant());

        p1.setYCoordinate(-1);
        System.out.println("Quadrant: " + p1.getQuadrant());

        p1.setXCoordinate(1);
        System.out.println("Quadrant: " + p1.getQuadrant());

        p1.setXCoordinate(0);
        p1.setYCoordinate(0);
        System.out.println("Quadrant: " + p1.getQuadrant());

        Demo d = new Demo();
        d.oneToTen();
        d.exerciseC();
        d.exerciseE();
        d.printBox(10, 5);
    }
}