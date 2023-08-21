import java.util.Arrays;

public class NumberSwapThree {
    public static void main(String[] args) {
        int[] arr = new int[]{45, 52, 11, 33, 48, 25};
        int[] swappedArr = swapArrayElements(arr);
        System.out.println("Original Array: " + Arrays.toString(arr));
        System.out.println("Swapped Array: " + Arrays.toString(swappedArr));
    }

    public static int[] swapArrayElements(int[] arr) {
        int[] swappedArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            swappedArr[i] = arr[i];
        }

        for (int i = 0; i < swappedArr.length / 2; i++) {
            int temp = swappedArr[i];
            swappedArr[i] = swappedArr[swappedArr.length - 1 - i];
            swappedArr[swappedArr.length - 1 - i] = temp;
        }

        return swappedArr;
    }
}
