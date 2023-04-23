package ch.hslu.test.sw10;

import ch.hslu.oop.sw10.Temperature;
import nl.jqno.equalsverifier.EqualsVerifier;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;

class TemperatureTest {
    @Test
    void testEquality() {
        EqualsVerifier
            .forClass(Temperature.class)
            .verify();
    }

    @Test
    void testCompareTo() {
        // arrange
        Temperature temp1 = Temperature.createFromCelsius(1);
        Temperature temp2 = Temperature.createFromCelsius(2);
        Temperature temp3 = Temperature.createFromCelsius(1);

        // assert
        assertThat(temp1.compareTo(temp2)).isNegative();
        assertThat(temp2.compareTo(temp1)).isPositive();
        assertThat(temp1.compareTo(temp3)).isZero();
    }

    @Test
    void testToString() {
        // arrange
        Temperature temp = Temperature.createFromCelsius(1);

        // assert
        assertThat(temp.toString()).isEqualTo("Temperature [temperatureInKelvin=274.15]");
    }

    @Test
    void testGetTemperatureCelsius() {
        // arrange
        Temperature temp = Temperature.createFromCelsius(1);

        // assert
        assertThat(temp.getTemperatureCelsius()).isEqualTo(1);
    }

    @Test
    void testGetTemperatureKelvin() {
        // arrange
        Temperature temp = Temperature.createFromCelsius(1);

        // assert
        assertThat(temp.getTemperatureKelvin()).isEqualTo(274.15);
    }

    @Test
    void testGetTemperatureFahrenheit() {
        // arrange
        Temperature temp = Temperature.createFromCelsius(1);

        // assert
        assertThat(temp.getTemperatureFahrenheit()).isEqualTo(33.8, within(0.0001));
    }

    @Test
    void testChangeTemperature() {
        // arrange
        Temperature temp = Temperature.createFromCelsius(1);

        // act
        Temperature changedTemp = temp.changeTemperature(1);

        // assert
        assertThat(changedTemp.getTemperatureCelsius()).isEqualTo(2);
    }

    @Test
    void testConvertKelvinToCelsius() {
        // assert
        assertThat(Temperature.convertKelvinToCelsius(1)).isEqualTo(-272.15);
    }

    @Test
    void testConvertCelsiusToKelvin() {
        // assert
        assertThat(Temperature.convertCelsiusToKelvin(0)).isEqualTo(273.15);
    }

    @Test
    void testCreateFromKelvin() {
        // assert
        assertThat(Temperature.createFromKelvin(1).getTemperatureCelsius()).isEqualTo(-272.15);
    }

    @Test
    void testIllegalArgumentExceptionIsThrownWhenTemperatureIsNegativeInKelvin() {
        // assert
        assertThatThrownBy(() -> Temperature.createFromKelvin(-1))
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessage("Temperature in kelvin must be greater than 0");
    }

    @Test
    void testIllegalArgumentExceptionIsThrownWhenTemperatureIsNegativeInCelsius() {
        // assert
        assertThatThrownBy(() -> Temperature.createFromCelsius(-1 - Temperature.KELVIN_OFFSET))
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessage("Temperature in kelvin must be greater than 0");
    }
}