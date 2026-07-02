import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        long sum = arr[N - 1];
        int min = arr[N - 1];

        double answer = 0.0;

        for (int i = N - 2; i >= 1; i--) {
            sum += arr[i];
            min = Math.min(min, arr[i]);

            double avg = (sum - min) / (double)(N - i - 1);
            answer = Math.max(answer, avg);
        }

        System.out.printf("%.2f\n", answer);
    }
}