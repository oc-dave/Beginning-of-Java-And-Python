package tdd;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertTrue;
import static org.testng.AssertJUnit.assertNotNull;



public class TurtleTest {
    private final boolean penIsUp = true;
    @Test
    public void testThatTurtleExists() {
        Turtle turtle = new Turtle();
        assertNotNull(turtle);
    }

    @Test
    public void turtlePenIsUpByDefaultTest() {
        Turtle turtle = new Turtle();
        assertNotNull(turtle.penIsUp());

    }

}
