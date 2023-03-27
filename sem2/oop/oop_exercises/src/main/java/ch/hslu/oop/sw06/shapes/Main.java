package ch.hslu.oop.sw06.shapes;

public class Main {

    public static void main(String[] args) {
        Shape shape1 = new Rectangle(10, 20, 30, 40);
        Shape shape2 = new Circle(10, 20, 30);

        shape1.move(10, 10);
        shape2.move(10, 10);

        Circle circle = (Circle) shape2;
        System.out.println(circle.getDiameter());
    }
}

