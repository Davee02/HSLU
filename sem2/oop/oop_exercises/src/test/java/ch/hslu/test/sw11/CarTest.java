package ch.hslu.test.sw11;

import ch.hslu.oop.sw11.car.Car;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;

public class CarTest {
    @Test
    void testSwitchOn() {
        // arrange
        Car car = new Car();

        // act
        car.switchOn();

        // assert
        assertThat(car.isSwitchedOn()).isTrue();
    }

    @Test
    void testSwitchOff() {
        // arrange
        Car car = new Car();

        // act
        car.switchOff();

        // assert
        assertThat(car.isSwitchedOff()).isTrue();
    }

    @Test
    void testGetSwitchCount() {
        // arrange
        Car car = new Car();

        // act
        car.switchOn();
        car.switchOff();

        // assert
        assertThat(car.getSwitchCount()).isEqualTo(2);
    }

    @Test
    void testSetName() {
        // arrange
        Car car = new Car();

        // act
        car.setName("MyCar");

        // assert
        assertThat(car.getName()).isEqualTo("MyCar");
    }
}
