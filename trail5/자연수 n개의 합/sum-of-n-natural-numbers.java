import java.util.*;

public class Main {
    static final long MAX_VALUE = Long.MAX_VALUE;

    static long s;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        s = sc.nextLong();

        System.out.println(search(s));
    }

    static long search(long target) {
        long left = 1, right = (long)1e10;
        long maxNum = 0;
        while (left <= right) {
            long mid = (left + right) / 2;
            if ((mid * (mid + 1)) / 2 <= target) {
                left = mid + 1;
                maxNum = Math.max(maxNum, mid);
            } else
                right = mid - 1;
        }
        return maxNum;
    }
}