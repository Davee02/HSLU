package ch.hslu.test.sw09;

import ch.hslu.oop.sw09.elements.AggregateState;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class AggregateStateTest {

    @Test
    void testToString() {
        // arrange
        AggregateState state = AggregateState.SOLID;

        // act
        String stateString = state.toString();

        // assert
        assertEquals("solid", stateString);
    }
}
