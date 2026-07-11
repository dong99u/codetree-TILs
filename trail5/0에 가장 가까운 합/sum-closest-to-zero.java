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

        Arrays.sort(arr);

        int j = n - 1;
        int answer = Math.abs(arr[0] + arr[n - 1]);
        for (int i = 0; i < n - 1; i++) {
            while (j - 1 >= 0 && i + 1 < j && arr[i] + arr[j] > 0) {
                answer = Math.min(answer, Math.abs(arr[i] + arr[j - 1]));
                j--;
            }
            if (i + 1 < j)
                answer = Math.min(answer, Math.abs(arr[i + 1] + arr[j]));
        }

        System.out.println(answer);

    }
}
