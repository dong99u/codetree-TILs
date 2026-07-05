import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] L = new int[n];
        int[] R = new int[n];
        L[0] = arr[0]; R[n - 1] = arr[n - 1];
        for (int i = 1; i < n; i++) {
            L[i] = Math.max(L[i - 1], arr[i]);
        }
        for (int i = n - 2; i >= 0; i--) {
            R[i] = Math.max(R[i + 1], arr[i]);
        }

        int answer = 0;
        for (int j = 2; j <= n - 3; j++) {
            int m = arr[j];
            int l = L[j - 2];
            int r = R[j + 2];
            answer = Math.max(answer, l + m + r);
        }

        System.out.println(answer);
    }
}
