package Example1;

import org.junit.Test;
import org.junit.Assert;

import java.util.Arrays;

public class ReturnArrayPositionTest {

    @Test
    public void testReturnArrayPosition() {
        int[] arr = new int[]{5, 18, 32, 3, 4};
        int[] expectedArr = new int[]{3, 4, 5, 18, 32};
        int[] actualArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            actualArr[i] = arr[i];
        }
        for (int i = 0; i < actualArr.length - 1; i++) {
            for (int j = 0; j < actualArr.length - i - 1; j++) {
                if (actualArr[j] > actualArr[j + 1]) {
                    int temp = actualArr[j];
                    actualArr[j] = actualArr[j + 1];
                    actualArr[j + 1] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(actualArr));
        Assert.assertArrayEquals(expectedArr, actualArr);
    }
}
