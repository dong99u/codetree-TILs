import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int m;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        System.out.println(search());
    }

    static int search() {
        int left = 1, right = (int)1e5;
        int maxNum = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (isValid(mid)) {
                left = mid + 1;
                maxNum = Math.max(maxNum, mid);
            } else
                right = mid - 1;
        }
        return maxNum;
    }

    static boolean isValid(int mid) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            count += arr[i] / mid;
        }
        return count >= m;
    }
}
