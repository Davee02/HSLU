package ch.hslu.test.sw07;

import ch.hslu.oop.sw07.Point;
import nl.jqno.equalsverifier.EqualsVerifier;
import nl.jqno.equalsverifier.Warning;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PointTest {
    @Test
    void testEquality() {
        EqualsVerifier
                .forClass(Point.class)
                .suppress(Warning.NONFINAL_FIELDS)
                .verify();
    }

    @Test
    void testCompareTo() {
        // arrange
        Point point1 = new Point(1, 1);
        Point point2 = new Point(2, 2);
        Point point3 = new Point(1, 1);

        // assert
        assertTrue(point1.compareTo(point2) < 0);
        assertTrue(point2.compareTo(point1) > 0);
        assertEquals(0, point1.compareTo(point3));
    }
}