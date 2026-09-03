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
        Arrays.sort(arr);

        int answer = search();
        System.out.println(answer);
    }

    public static int search() {
        int left = 1, right = arr[n - 1] - arr[0];
        int maxRet = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (possible(mid)) {
                left = mid + 1;
                maxRet = Math.max(maxRet, mid);
            } else {
                right = mid - 1;
            }
        }

        return maxRet;
    }

    public static boolean possible(int x) {
        int left = 0;
        int cnt = 1; // 점의 개수
        int right = left + 1;
        while (right < n) {
            if (arr[right] - arr[left] >= x) {
                cnt++;
                left = right;
            }
            right++;
        }

        if (cnt >= m)
            return true;
        else
            return false;
    }
}
