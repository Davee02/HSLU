package ch.hslu.test.sw07;

import ch.hslu.oop.sw07.Temperatur;
import nl.jqno.equalsverifier.EqualsVerifier;
import nl.jqno.equalsverifier.Warning;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TemperaturTest {
    @Test
    void testEquality() {
        EqualsVerifier
                .forClass(Temperatur.class)
                .suppress(Warning.NONFINAL_FIELDS)
                .verify();
    }

    @Test
    void testCompareTo() {
        // arrange
        Temperatur temp1 = new Temperatur(1);
        Temperatur temp2 = new Temperatur(2);
        Temperatur temp3 = new Temperatur(1);

        // assert
        assertTrue(temp1.compareTo(temp2) < 0);
        assertTrue(temp2.compareTo(temp1) > 0);
        assertEquals(0, temp1.compareTo(temp3));
    }
}