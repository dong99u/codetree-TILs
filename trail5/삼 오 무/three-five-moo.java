import java.util.*;

public class Main {
    static long n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextLong();
        System.out.println(search());
    }

    static long search() {
        long left = 1, right = (long)1e13;
        long minNum = (long)1e13;
        while (left <= right) {
            long mid = (left + right) / 2;
            if (isValid(mid)) {
                right = mid - 1;
                minNum = Math.min(minNum, mid);
            } else
                left = mid + 1;
        }
        return minNum;
    }

    static boolean isValid(long mid) {
        long countTwo = mid / 3;
        long countFive = mid / 5;
        long countBoth = mid / 15;

        return mid - countTwo - countFive + countBoth >= n;
    }
}
