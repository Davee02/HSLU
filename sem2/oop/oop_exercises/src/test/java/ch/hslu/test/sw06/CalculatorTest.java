package ch.hslu.test.sw06;

import ch.hslu.oop.sw06.calculator.Calculator;
import ch.hslu.oop.sw06.calculator.ICalculator;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    @Test
    public void testAddPositiveNumbers() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }

    @Test
    public void testAddNegativeNumbers() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(-2, -3);
        assertEquals(-5, result);
    }

    @Test
    public void testAddNegativeAndPositiveNumbers() {
        Calculator calculator = new Calculator();
        int result = calculator.add(-2, 3);
        assertEquals(1, result);
    }

    @Test
    public void testAddZero() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(2, 0);
        assertEquals(2, result);
    }

    @Test
    public void testAddLargeNumbers() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(1000000, 2000000);
        assertEquals(3000000, result);
    }

    @Test
    public void testAddPositiveOverflow() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(Integer.MAX_VALUE, 1);
        assertEquals(Integer.MIN_VALUE, result);
    }

    @Test
    public void testAddNegativeOverflow() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(Integer.MIN_VALUE, -1);
        assertEquals(Integer.MAX_VALUE, result);
    }

    @Test
    public void testAddMaxValue() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(Integer.MAX_VALUE, 0);
        assertEquals(Integer.MAX_VALUE, result);
    }

    @Test
    public void testAddMinValue() {
        ICalculator calculator = new Calculator();
        int result = calculator.add(Integer.MIN_VALUE, 0);
        assertEquals(Integer.MIN_VALUE, result);
    }
}