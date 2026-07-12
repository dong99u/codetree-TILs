import java.util.*;

public class Main {
    static long n;
    static long k;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextLong();
        k = sc.nextLong();

        System.out.println(search());
    }

    static long search() {
        long left = 1, right = (long)n * n;
        long minNum = n * n;
        while (left <= right) {
            long mid = (left + right) / 2;
            if (getCount(mid) >= k) {
                right = mid - 1;
                minNum = Math.min(minNum, mid);
            } else
                left = mid + 1;
        }
        return minNum;
    }

    static long getCount(long mid) {
        long count = 0;
        for (int i = 1; i < n + 1; i++) {
            count += Math.min(n, mid / i);
        }
        return count;
    }
}
