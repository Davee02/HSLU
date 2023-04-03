package ch.hslu.test.sw07;

import ch.hslu.oop.sw07.Person;
import nl.jqno.equalsverifier.EqualsVerifier;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PersonTest {
    @Test
    void testConstructorAssignedValuesAreCorrect() {
        // arrange
        long id = 1;
        String firstname = "John";
        String lastname = "Doe";

        // act
        Person person = new Person(id, firstname, lastname);

        // assert
        assertEquals(id, person.getId());
        assertEquals(firstname, person.getFirstname());
        assertEquals(lastname, person.getLastname());
    }

    @Test
    void testEquality() {
        EqualsVerifier
                .forClass(Person.class)
                .withIgnoredFields("firstname", "lastname")
                .verify();
    }

    @Test
    void testEquals() {
        // arrange
        long id = 1;
        String firstname = "John";
        String lastname = "Doe";

        // act
        Person person = new Person(id, firstname, lastname);

        // assert
        assertEquals(person, person);
    }

    @Test
    void testNotEquals() {
        // arrange
        long id = 1;
        String firstname = "John";
        String lastname = "Doe";

        // act
        Person person = new Person(id, firstname, lastname);

        // assert
        assertNotEquals(person, null);
    }

    @Test
    void testToString() {
        // arrange
        long id = 1;
        String firstname = "John";
        String lastname = "Doe";

        // act
        Person person = new Person(id, firstname, lastname);

        // assert
        assertEquals("Person [id=" + id + ", firstname=" + firstname + ", lastname=" + lastname + "]", person.toString());
    }

    @Test
    void testHashCode() {
        // arrange
        long id = 1;
        String firstname = "John";
        String lastname = "Doe";

        // act
        Person person = new Person(id, firstname, lastname);

        // assert
        assertEquals(Long.hashCode(id), person.hashCode());
    }

    @Test
    void testCompareTo() {
        // arrange
        long id1 = 1;
        String firstname1 = "John";
        String lastname1 = "Doe";
        Person person1 = new Person(id1, firstname1, lastname1);

        long id2 = 2;
        String firstname2 = "Jane";
        String lastname2 = "Doe";
        Person person2 = new Person(id2, firstname2, lastname2);

        long id3 = 1;
        String firstname3 = "John";
        String lastname3 = "Doe";
        Person person3 = new Person(id3, firstname3, lastname3);

        // assert
        assertTrue(person1.compareTo(person2) < 0);
        assertTrue(person2.compareTo(person1) > 0);
        assertEquals(0, person1.compareTo(person3));
    }
}