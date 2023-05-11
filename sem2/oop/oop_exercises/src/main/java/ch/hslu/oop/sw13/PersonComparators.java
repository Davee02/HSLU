package ch.hslu.oop.sw13;

import java.util.Comparator;

public final class PersonComparators {
    public static final Comparator<Person> firstNameComparator = (p1, p2) -> p1.getFirstname().compareTo(p2.getFirstname());
    public static final Comparator<Person> lastNameComparator = (p1, p2) -> p1.getLastname().compareTo(p2.getLastname());
    public static final Comparator<Person> lastThenFirstNameComparator = (p1, p2) -> lastNameComparator.thenComparing(firstNameComparator).compare(p1, p2);
}
