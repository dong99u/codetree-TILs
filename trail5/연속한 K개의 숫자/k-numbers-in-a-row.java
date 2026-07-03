import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int b = sc.nextInt();

        int[] arr = new int[n + 1];
        for (int i = 0; i < b; i++) {
            int idx = sc.nextInt();
            arr[idx] = 1;
        }

        int[] prefixSum = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }

        int answer = Integer.MAX_VALUE;
        for (int i = k; i < n + 1; i++) {
            answer = Math.min(answer, prefixSum[i] - prefixSum[i - k]);
        }

        System.out.println(answer);
    }

}
