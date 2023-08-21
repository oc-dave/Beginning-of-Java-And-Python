package tdd;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class FoodTest {

    @Test
    public void canAdd(){
        Food rice = new Food("Rice", 20);
        Food beans = new Food(" beans", 10);
        rice.getPrice();
        beans.getPrice();
        System.out.println(rice.getPrice());
    }

}
