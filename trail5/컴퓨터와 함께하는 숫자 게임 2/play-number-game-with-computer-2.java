import java.util.*;
import java.io.*;

public class Main {
    static long m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        m = Long.parseLong(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        int minCount = (int)1e9;
        int maxCount = -1;
        for (long target = a; target <= b; target++) {
            int result = search(target);
            minCount = Math.min(minCount, result);
            maxCount = Math.max(maxCount, result);
        }
        System.out.println(minCount + " " + maxCount);
    }

    static int search(long target) {
        int count = 1;
        long left = 1, right = m;
        while (left <= right) {
            long mid = (left + right) / 2;
            if (mid == target)
                return count;

            if (mid > target)
                right = mid - 1;
            else
                left = mid + 1;
            count++;
        }
        return count;
    }
}
