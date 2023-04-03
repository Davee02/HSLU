package ch.hslu.oop.sw07;

public class Person implements Comparable<Person> {
    private final long id;
    private String firstname;
    private String lastname;

    public Person(long id, String firstname, String lastname) {
        this.id = id;
        this.firstname = firstname;
        this.lastname = lastname;
    }

    public final long getId() {
        return id;
    }

    public final String getFirstname() {
        return firstname;
    }

    public final void setFirstname(final String firstname) {
        this.firstname = firstname;
    }

    public final String getLastname() {
        return lastname;
    }

    public final void setLastname(final String lastname) {
        this.lastname = lastname;
    }

    @Override
    public String toString() {
        return "Person [id=" + id + ", firstname=" + firstname + ", lastname=" + lastname + "]";
    }

    @Override
    public final boolean equals(final Object object) {
        if (this == object) {
            return true;
        }

        return object instanceof Person p
                && this.id == p.id;
    }

    @Override
    public final int hashCode() {
        return Long.hashCode(id);
    }

    @Override
    public final int compareTo(final Person other) {
        return Long.compare(this.id, other.id);
    }
}
