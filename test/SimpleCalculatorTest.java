import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SimpleCalculatorTest {

    @Test
    void fivePlusFiveShouldEqualTen(){
        var calculator = new SimpleCalculator();
        assertEquals(10, calculator.add(5,5));
    }

}