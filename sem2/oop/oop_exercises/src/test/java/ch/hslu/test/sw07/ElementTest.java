package ch.hslu.test.sw07;

import ch.hslu.oop.sw07.Elements.Lead;
import ch.hslu.oop.sw07.Elements.Mercury;
import ch.hslu.oop.sw07.Elements.Nitrogen;
import nl.jqno.equalsverifier.EqualsVerifier;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ElementTest {
    @Test
    void testLeadEquality() {
        EqualsVerifier
                .forClass(Lead.class)
                .verify();
    }

    @Test
    void testMercuryEquality() {
        EqualsVerifier
                .forClass(Mercury.class)
                .verify();
    }

    @Test
    void testNitrogenEquality() {
        EqualsVerifier
                .forClass(Nitrogen.class)
                .verify();
    }

    @Test
    void testCompareTo() {
        // arrange
        Lead lead = new Lead();
        Mercury mercury = new Mercury();
        Nitrogen nitrogen = new Nitrogen();

        // assert
        assertTrue(lead.compareTo(mercury) > 0);
        assertTrue(mercury.compareTo(lead) < 0);
        assertTrue(lead.compareTo(nitrogen) > 0);
        assertTrue(nitrogen.compareTo(lead) < 0);
        assertTrue(mercury.compareTo(nitrogen) < 0);
        assertTrue(nitrogen.compareTo(mercury) > 0);

        assertEquals(0, lead.compareTo(lead));
        assertEquals(0, mercury.compareTo(mercury));
        assertEquals(0, nitrogen.compareTo(nitrogen));
    }
}