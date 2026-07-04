import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            arr[i] = new int[] {x, y};
        }

        int[] L = new int[n];
        int[] R = new int[n];
        for (int i = 1; i < n; i++) {
            L[i] = L[i - 1] + getDistance(arr, i, i - 1);
        }
        for (int i = n - 2; i >= 0; i--) {
            R[i] = R[i + 1] + getDistance(arr, i, i + 1);
        }

        int answer = Integer.MAX_VALUE;

        // 제외할 체크포인트 선택
        for (int i = 1; i < n - 1; i++) {
            answer = Math.min(answer, L[i - 1] + R[i + 1] + getDistance(arr, i - 1, i + 1));
        }

        System.out.println(answer);
    }

    static int getDistance(int[][] arr, int i, int j) {
        int[] p1 = arr[i];
        int[] p2 = arr[j];

        return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
    }
}
