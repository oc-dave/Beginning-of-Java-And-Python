package tdd;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {


    @Test
    public void testThatCalculatorExists() {
        Calculator calculator = new Calculator();

        assertNotNull(calculator);


    }

    @Test
    public void testThatCalculatorCanBePoweredOn() {
        Calculator calculator = new Calculator();
        calculator.power();
        assertTrue(calculator.isOn());
    }

    @Test
    public void testThatCalculatorCanBePoweredOff() {
        Calculator calculator = new Calculator();
            calculator.power();
            assertTrue(calculator.isOff());
            calculator.power();


    }

}
