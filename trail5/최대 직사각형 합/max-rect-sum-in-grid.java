import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int[] colSum = new int[n];
            for (int j = i; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    colSum[k] += matrix[j][k];
                }
                int best = colSum[0], cur = colSum[0];
                for (int k = 1; k < n; k++) {
                    cur = Math.max(colSum[k], cur + colSum[k]);
                    best = Math.max(cur, best);
                }
                answer = Math.max(answer, best);
            }
        }
        System.out.println(answer);

    }
}
