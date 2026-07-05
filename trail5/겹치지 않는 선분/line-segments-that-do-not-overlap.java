import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            arr[i] = new int[] {x1, x2};
        }
        Arrays.sort(arr, Comparator.comparingInt(e -> e[0]));

        int[] L = new int[n];
        int[] R = new int[n];
        L[0] = arr[0][1]; R[n - 1] = arr[n - 1][1];
        for (int i = 1; i < n; i++) {
            L[i] = Math.max(L[i - 1], arr[i][1]);
        }
        for (int i = n - 2; i >= 0; i--) {
            R[i] = Math.min(R[i + 1], arr[i][1]);
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            boolean isLeftOk = (i == 0) || (arr[i][1] > L[i - 1]);
            boolean isRightOk = (i == n - 1) || (arr[i][1] < R[i + 1]);

            if (isLeftOk && isRightOk) answer++;
        }

        System.out.println(answer);
    }
}
