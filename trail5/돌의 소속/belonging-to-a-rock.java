import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();
        int q = sc.nextInt();

        int[][] arr = new int[n + 1][4];
        for (int i = 1; i < n + 1; i++) {
            arr[i][sc.nextInt()] = 1;
        }

        int[][] prefixSum = new int[n + 1][4];
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < 4; j++) {
                prefixSum[i][j] = prefixSum[i - 1][j] + arr[i][j];
            }
        }

        for (int i = 0; i < q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            for (int j = 1; j < 4; j++) {
                sb.append(prefixSum[b][j] - prefixSum[a - 1][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
