public class Main {
    public static void main(String[] args) {
//        Engine engine = new Engine();
//        engine.switchOn();
//        System.out.println(engine.isSwitchedOn());
//        System.out.println(engine.isSwitchedOff());
//        engine.switchOff();
//        System.out.println(engine.isSwitchedOn());
//        System.out.println(engine.isSwitchedOff());
//
//        engine.setRotationsPerMinute(1000);
//        System.out.println(engine.getRotationsPerMinute());
//        System.out.println(engine.isSwitchedOn());
//        System.out.println(engine.isSwitchedOff());
//
//        engine.setRotationsPerMinute(0);
//        System.out.println(engine.getRotationsPerMinute());
//        System.out.println(engine.isSwitchedOn());
//        System.out.println(engine.isSwitchedOff());
//
//        Car car = new Car();
//        car.switchOn();
//        System.out.println(car.isSwitchedOn());
//        System.out.println(car.isSwitchedOff());
//        car.switchOff();

        Line line = new Line(1, 2, 3, 4);
        System.out.println(line.getStartPoint().getXCoordinate());
        System.out.println(line.getStartPoint().getYCoordinate());
        System.out.println(line.getEndPoint().getXCoordinate());
        System.out.println(line.getEndPoint().getYCoordinate());
        System.out.println();

        line.setStartPoint(5, 6);
        System.out.println(line.getStartPoint().getXCoordinate());
        System.out.println(line.getStartPoint().getYCoordinate());
        System.out.println(line.getEndPoint().getXCoordinate());
        System.out.println(line.getEndPoint().getYCoordinate());
        System.out.println();

        line.setEndPoint(7, 8);
        System.out.println(line.getStartPoint().getXCoordinate());
        System.out.println(line.getStartPoint().getYCoordinate());
        System.out.println(line.getEndPoint().getXCoordinate());
        System.out.println(line.getEndPoint().getYCoordinate());
        System.out.println();

        line.getEndPoint().setXCoordinate(9);
        line.getEndPoint().setYCoordinate(10);
        System.out.println(line.getEndPoint().getXCoordinate());
        System.out.println(line.getEndPoint().getYCoordinate());
    }
}