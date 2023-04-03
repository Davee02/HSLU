package ch.hslu.oop.sw07;

import java.util.Comparator;

public class PersonNameComparator implements Comparator<Person> {
    @Override
    public int compare(Person p1, Person p2) {
        return Comparator.comparing(Person::getLastname)
                .thenComparing(Person::getFirstname)
                .compare(p1, p2);
    }
}
