import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][][] box = new int[n + 1][m + 1][3];

        for (int i = 1; i < n + 1; i++) {
            char[] chars = br.readLine().toCharArray();
            for (int j = 1; j < m + 1; j++) {
                box[i][j][chars[j - 1] - 'a'] = 1;
            }
        }

        int[][][] prefixSum = new int[n + 1][m + 1][3];
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                for (int l = 0; l < 3; l++) {
                    prefixSum[i][j][l] =
                        prefixSum[i - 1][j][l] + prefixSum[i][j - 1][l] - prefixSum[i - 1][j - 1][l] + box[i][j][l];
                }
            }
        }

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int r1 = Integer.parseInt(st.nextToken()), c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken()), c2 = Integer.parseInt(st.nextToken());

            for (int j = 0; j < 3; j++) {
                int result =
                    prefixSum[r2][c2][j] - prefixSum[r2][c1 - 1][j] - prefixSum[r1 - 1][c2][j] + prefixSum[r1 - 1][c1
                        - 1][j];
                sb.append(result).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
