package tdd;

public class Food {

    private final String name;
    private int price;

    public Food(String name, int price) {
        this.name = name;
        this.price = price;
    }

    public boolean getPrice() {
        System.out.println(this.price);
        return true;
    }
}
