import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int j = 0;
        int answer = 0;
        int sum = arr[0];
        
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && sum < m) {
                sum += arr[j + 1];
                j++;
            }
            if (sum == m)
                answer++;
            sum -= arr[i];
        }
        System.out.println(answer);
    }
}