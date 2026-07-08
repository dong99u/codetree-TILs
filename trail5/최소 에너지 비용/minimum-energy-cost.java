import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dists = new int[n - 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n - 1; i++) {
            dists[i] = Integer.parseInt(st.nextToken());
        }

        int[] costs = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            costs[i] = Integer.parseInt(st.nextToken());
        }

        int[] L = new int[n];
        L[0] = costs[0];
        for (int i = 1; i < n; i++) {
            L[i] = Math.min(L[i - 1], costs[i]);
        }

        long answer = 0;
        for (int i = 0; i < n - 1; i++) {
            answer += (long)L[i] * dists[i];
        }

        System.out.println(answer);
    }
}