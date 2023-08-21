package Example1;

import java.util.ArrayList;
import java.util.List;

public class Problem {
    private String name;
    private String type;
    private boolean status;

    public Problem(String name, String type) {
        this.name = name;
        this.type = type;
        this.status = false;
    }

    public boolean isSolved() {
        return status;
    }

    public void solved() {
        this.status = true;
    }

    public class Person {
        private List<Person> problems;
    }


}