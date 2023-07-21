import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SimpleCalculatorTest {

    @Test
    void fivePlusFiveShouldEqualTen(){
        var calculator = new SimpleCalculator();
        assertEquals(10, calculator.add(5,5));
    }

    @Test
    void sixMultiplyEightEqualsFortyEight(){
        var calculator = new SimpleCalculator();
        assertTrue(true);
        assertEquals(48,32, calculator.multiply(6, 8));

    }
}