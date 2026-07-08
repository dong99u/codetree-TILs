import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            arr[i] = sc.nextInt();
        }

        int[] prefixSum = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            prefixSum[i] = (prefixSum[i - 1] + arr[i]) % 7;
        }

        int[] L = new int[7];
        Arrays.fill(L, -1);

        int answer = 0;
        for (int i = 0; i < n + 1; i++) {
            int j = prefixSum[i] % 7;
            if (L[j] == -1) {
                L[j] = i;
            } else {
                answer = Math.max(answer, i - L[j]);
            }
        }
        System.out.println(answer);

    }
}
