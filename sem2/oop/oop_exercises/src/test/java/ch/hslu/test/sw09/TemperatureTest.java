package ch.hslu.test.sw09;

import ch.hslu.oop.sw09.Temperature;
import nl.jqno.equalsverifier.EqualsVerifier;
import nl.jqno.equalsverifier.Warning;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class TemperatureTest {
    @Test
    void testEquality() {
        EqualsVerifier
                .forClass(Temperature.class)
                .suppress(Warning.NONFINAL_FIELDS)
                .verify();
    }

    @Test
    void testCompareTo() {
        // arrange
        Temperature temp1 = new Temperature(1);
        Temperature temp2 = new Temperature(2);
        Temperature temp3 = new Temperature(1);

        // assert
        assertTrue(temp1.compareTo(temp2) < 0);
        assertTrue(temp2.compareTo(temp1) > 0);
        assertEquals(0, temp1.compareTo(temp3));
    }

    @Test
    void testToString() {
        // arrange
        Temperature temp = new Temperature(1);

        // assert
        assertEquals("Temperatur [earthTemperatureCelsius=1.0]", temp.toString());
    }

    @Test
    void testGetTemperatureCelsius() {
        // arrange
        Temperature temp = new Temperature(1);

        // assert
        assertEquals(1, temp.getTemperatureCelsius());
    }

    @Test
    void testSetTemperatureCelsius() {
        // arrange
        Temperature temp = new Temperature(1);

        // act
        temp.setTemperatureCelsius(2);

        // assert
        assertEquals(2, temp.getTemperatureCelsius());
    }

    @Test
    void testGetTemperatureKelvin() {
        // arrange
        Temperature temp = new Temperature(1);

        // assert
        assertEquals(274.15, temp.getTemperatureKelvin());
    }

    @Test
    void testGetTemperatureFahrenheit() {
        // arrange
        Temperature temp = new Temperature(1);

        // assert
        assertEquals(33.8, temp.getTemperatureFahrenheit());
    }

    @Test
    void testChangeTemperature() {
        // arrange
        Temperature temp = new Temperature(1);

        // act
        temp.changeTemperature(1);

        // assert
        assertEquals(2, temp.getTemperatureCelsius());
    }

    @Test
    void testConvertKelvinToCelsius() {
        // assert
        assertEquals(-272.15, Temperature.convertKelvinToCelsius(1));
    }

    @Test
    void testConvertCelsiusToKelvin() {
        // assert
        assertEquals(273.15, Temperature.convertCelsiusToKelvin(0));
    }

}