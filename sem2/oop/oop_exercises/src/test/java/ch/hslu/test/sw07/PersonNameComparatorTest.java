package ch.hslu.test.sw07;

import ch.hslu.oop.sw07.Person;
import ch.hslu.oop.sw07.PersonNameComparator;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PersonNameComparatorTest {

    @Test
    void testNameComparison() {
        Person p1 = new Person(1, "Hans", "Muster");
        Person p2 = new Person(2, "Hans", "Müller");
        Person p3 = new Person(3, "Peter", "Müller");
        Person p4 = new Person(4, "Hans", "Muster");

        PersonNameComparator comparator = new PersonNameComparator();

        assertTrue(comparator.compare(p1, p2) < 0);
        assertTrue(comparator.compare(p2, p3) < 0);
        assertTrue(comparator.compare(p3, p4) > 0);
        assertTrue(comparator.compare(p1, p4) == 0);
    }
}