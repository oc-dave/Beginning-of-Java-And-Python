package Example1;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;

public class NumberSwapTestThree {

    @Test
    public void testNumberSwapThree() {
        int[] arr = new int[]{45, 52, 11, 33, 48, 25};
        int[] expectedArr = new int[]{25, 48, 33, 11, 52, 45};
        int[] actualArr = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            actualArr[i] = arr[i];
        }

        for (int i = 0; i < actualArr.length / 2; i++) {
            int temp = actualArr[i];
            actualArr[i] = actualArr[actualArr.length - 1 - i];
            actualArr[actualArr.length - 1 - i] = temp;
        }
        System.out.println(Arrays.toString(actualArr));
        assertArrayEquals(expectedArr, actualArr);
    }
}
