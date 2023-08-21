package Example1;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;

public class NumberSwapTestTwo {

    @Test
    public void testNumberSwapTwo(){
        int[] arr = new int[]{45, 52, 11, 33, 48, 25};
        int[] expectedArr = new int[]{45, 52, 33, 11, 48, 25};
        int[] actualArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            actualArr[i] = arr[i];
        }
        for (int i = 0; i < actualArr.length - 1; i++) {
            if (i % 2 == 0 ) {
                int temp = actualArr[i];
                actualArr[i] = actualArr[i + 1];
                actualArr[i + 1] = temp;
            }
        }
        System.out.println(Arrays.toString(actualArr));
        assertArrayEquals(expectedArr, actualArr);
    }
}
