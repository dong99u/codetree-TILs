import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        char[] arr = br.readLine().toCharArray();

        int[] L = new int[n];
        int[] R = new int[n];
        L[0] = arr[0] == 'C' ? 1 : 0;
        R[n - 1] = arr[n - 1] == 'W' ? 1 : 0;
        for (int i = 1; i < n; i++) {
            L[i] = L[i - 1] + (arr[i] == 'C' ? 1 : 0);
        }
        for (int i = n - 2; i >= 0; i--) {
            R[i] = R[i + 1] + (arr[i] == 'W' ? 1 : 0);
        }

        long answer = 0;
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] == 'O') {
                answer += L[i - 1] * R[i + 1];
            }
        }
        System.out.println(answer);
    }
}
