package ch.hslu.test.sw06;

import ch.hslu.oop.sw06.tests.Demo;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DemoTest {

    @Test
    void testMaxReturnsBiggerNumberWhenFirstNumberIsBigger() {
        // arrange
        int a = 5;
        int b = 3;

        // act
        int result = new Demo().max(a, b);

        // assert
        assertEquals(a, result);
    }

    @Test
    void testMaxReturnsBiggerNumberWhenSecondNumberIsBigger() {
        // arrange
        int a = 3;
        int b = 5;

        // act
        int result = new Demo().max(a, b);

        // assert
        assertEquals(b, result);
    }

    @Test
    void testMaxReturnsInputIfBothAreEqual() {
        // arrange
        int a = 3;
        int b = 3;

        // act
        int result = new Demo().max(a, b);

        // assert
        assertEquals(b, result);
    }
}