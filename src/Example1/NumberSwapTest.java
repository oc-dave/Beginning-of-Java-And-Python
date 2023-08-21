package Example1;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;

public class NumberSwapTest {

    @Test
    public void testNumberSwap() {
        int[] arr = new int[]{1, 2, 3, 4, 5, 6};
        int[] expectedArr = new int[]{2, 1, 4, 3, 6, 5};
        int[] actualArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            actualArr[i] = arr[i];
        }
        for (int i = 0; i < actualArr.length - 1; i++) {
            if (i % 2 == 0) {
                int temp = actualArr[i];
                actualArr[i] = actualArr[i + 1];
                actualArr[i + 1] = temp;
            }
        }
        System.out.println(Arrays.toString(actualArr));
        assertArrayEquals(expectedArr, actualArr);
    }
}
