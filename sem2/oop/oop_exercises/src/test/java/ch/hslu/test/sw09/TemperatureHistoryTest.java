package ch.hslu.test.sw09;

import ch.hslu.oop.sw09.Temperature;
import ch.hslu.oop.sw09.TemperatureHistory;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class TemperatureHistoryTest {
    @Test
    void testAdd() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();
        Temperature temp = new Temperature(1);

        // act
        history.add(temp);

        // assert
        assertEquals(1, history.getCount());
    }

    @Test
    void testClear() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();
        Temperature temp = new Temperature(1);
        history.add(temp);

        // act
        history.clear();

        // assert
        assertEquals(0, history.getCount());
    }

    @Test
    void testGetMax() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();
        Temperature temp1 = new Temperature(1);
        Temperature temp2 = new Temperature(3);
        Temperature temp3 = new Temperature(2);
        history.add(temp1);
        history.add(temp2);
        history.add(temp3);

        // act
        Temperature max = history.getMax();

        // assert
        assertEquals(3, max.getTemperatureCelsius());
    }

    @Test
    void testGetMaxNoValues() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();

        // act
        Temperature max = history.getMax();

        // assert
        assertEquals(0, max.getTemperatureCelsius());
    }

    @Test
    void testGetMin() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();
        Temperature temp1 = new Temperature(1);
        Temperature temp2 = new Temperature(3);
        Temperature temp3 = new Temperature(2);
        history.add(temp1);
        history.add(temp2);
        history.add(temp3);

        // act
        Temperature max = history.getMin();

        // assert
        assertEquals(1, max.getTemperatureCelsius());
    }

    @Test
    void testGetMinNoValues() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();

        // act
        Temperature max = history.getMin();

        // assert
        assertEquals(0, max.getTemperatureCelsius());
    }

    @Test
    void testGetAverage() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();
        Temperature temp1 = new Temperature(1);
        Temperature temp2 = new Temperature(3);
        Temperature temp3 = new Temperature(2);
        history.add(temp1);
        history.add(temp2);
        history.add(temp3);

        // act
        double average = history.getAverage();

        // assert
        assertEquals(2, average);
    }

    @Test
    void testGetAverageNoValues() {
        // arrange
        TemperatureHistory history = new TemperatureHistory();

        // act
        double average = history.getAverage();

        // assert
        assertEquals(0, average);
    }
}
