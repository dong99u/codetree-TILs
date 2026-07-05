import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] L = new int[n];
        int[] R = new int[n];
        L[0] = arr[0];
        R[n - 1] = arr[n - 1];
        for (int i = 1; i < n; i++) {
            L[i] = Math.max(L[i - 1], arr[i]);
        }
        for (int i = n - 2; i >= 0; i--) {
            R[i] = Math.max(R[i + 1], arr[i]);
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;

            int result = Math.max(L[a - 1], R[b + 1]);
            sb.append(result).append("\n");
        }

        System.out.println(sb);
    }
}
