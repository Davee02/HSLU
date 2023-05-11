package ch.hslu.test.sw13;

import ch.hslu.oop.sw13.PersonComparators;
import org.junit.jupiter.api.Test;

import java.time.format.DateTimeParseException;

import static org.assertj.core.api.Assertions.*;

public class PersonComparatorsTest {
    @Test
    void testFirstNameComparator() {
        // arrange
        var p1 = new ch.hslu.oop.sw13.Person(1, "Hans", "Muster");
        var p2 = new ch.hslu.oop.sw13.Person(2, "Peter", "Mueller");
        var p3 = new ch.hslu.oop.sw13.Person(3, "Hans", "Meyer");
        var p4 = new ch.hslu.oop.sw13.Person(4, "Albert", "Meyer");

        // act
        var result = PersonComparators.firstNameComparator.compare(p1, p2);
        var result2 = PersonComparators.firstNameComparator.compare(p1, p3);
        var result3 = PersonComparators.firstNameComparator.compare(p1, p4);

        // assert
        assertThat(result).isNegative();
        assertThat(result2).isEqualTo(0);
        assertThat(result3).isPositive();
    }

    @Test
    void testLastNameComparator() {
        // arrange
        var p1 = new ch.hslu.oop.sw13.Person(1, "Hans", "Muster");
        var p2 = new ch.hslu.oop.sw13.Person(2, "Peter", "Mueller");
        var p3 = new ch.hslu.oop.sw13.Person(3, "Hans", "Muster");
        var p4 = new ch.hslu.oop.sw13.Person(3, "Hans", "Zitadel");

        // act
        var result = PersonComparators.lastNameComparator.compare(p1, p2);
        var result2 = PersonComparators.lastNameComparator.compare(p1, p3);
        var result3 = PersonComparators.lastNameComparator.compare(p1, p4);

        // assert
        assertThat(result).isPositive();
        assertThat(result2).isEqualTo(0);
        assertThat(result3).isNegative();
    }

    @Test
    void testLastThenFirstNameComparator() {
        // arrange
        var p1 = new ch.hslu.oop.sw13.Person(1, "Hans", "Muster");
        var p2 = new ch.hslu.oop.sw13.Person(2, "Peter", "Mueller");
        var p3 = new ch.hslu.oop.sw13.Person(3, "Hans", "Muster");
        var p4 = new ch.hslu.oop.sw13.Person(3, "Hans", "Zitadel");
        var p5 = new ch.hslu.oop.sw13.Person(4, "Albert", "Zitadel");

        // act
        var result = PersonComparators.lastThenFirstNameComparator.compare(p1, p2);
        var result2 = PersonComparators.lastThenFirstNameComparator.compare(p1, p3);
        var result3 = PersonComparators.lastThenFirstNameComparator.compare(p1, p4);
        var result4 = PersonComparators.lastThenFirstNameComparator.compare(p4, p5);

        // assert
        assertThat(result).isPositive();
        assertThat(result2).isEqualTo(0);
        assertThat(result3).isNegative();
        assertThat(result4).isPositive();
    }
}
