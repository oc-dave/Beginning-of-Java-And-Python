package tdd;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AccountTest {

    @Test
    public void canDepositIntoAccountTest(){

        Account davidAccount = new Account();
        davidAccount.deposit(0);
        int currentBalance = davidAccount.getBalance("2678");
        assertEquals(0, currentBalance);

        davidAccount.deposit(5000);

        int newBalance = davidAccount.getBalance("2678");
        assertEquals(5000, newBalance);


    }



    @Test
    public void canDepositTwiceTest(){
        Account davidAccount = new Account();
        davidAccount.deposit(3000);
        int currentBalance = davidAccount.getBalance("2678");
        assertEquals(3000, currentBalance);

        davidAccount.deposit(2000);

        int newBalance = davidAccount.getBalance("2678"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         );
        assertEquals(5000, newBalance);


    }


    @Test
    public void canDepositNegativeBalance(){
        Account davidAccount = new Account();
        davidAccount.deposit(1000);
        int currentBalance = davidAccount.getBalance("2678");
        assertEquals(1000, currentBalance);

        davidAccount.deposit(-2000);

        int newBalance = davidAccount.getBalance("2678");
        assertEquals(-1000, newBalance);
    }

    @Test
    public void canWithdraw(){
        Account davidAccount = new Account();
        davidAccount.deposit(5000);
        int currentBalance = davidAccount.getBalance("2678");
        assertEquals(5000, currentBalance);

        davidAccount.withdraw(3000);
        int newBalance = davidAccount.getBalance("2678");
        assertEquals(2000, newBalance);


    }

}

