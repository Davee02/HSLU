package ch.hslu.test.sw09;

import ch.hslu.oop.sw09.elements.Lead;
import ch.hslu.oop.sw09.elements.AggregateState;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class LeadTest {

    @Test
    void testGetSolidState() {
        // arrange
        Lead lead = new Lead();

        // act
        String state = lead.getAggregateState(15);

        // assert
        assertEquals("Pb has the aggregate state solid at 15.00°C", state);
    }

    @Test
    void testGetLiquidState() {
        // arrange
        Lead lead = new Lead();

        // act
        String state = lead.getAggregateState(400);

        // assert
        assertEquals("Pb has the aggregate state liquid at 400.00°C", state);
    }

    @Test
    void testGetGasState() {
        // arrange
        Lead lead = new Lead();

        // act
        String state = lead.getAggregateState(1800);

        // assert
        assertEquals("Pb has the aggregate state gas at 1800.00°C", state);
    }
}
