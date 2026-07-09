import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        int answer = 0;
        int j = n - 1;
        for (int i = 0; i < n; i++) {
            while (j > 0 && i < j && arr[i] + arr[j] > k)
                j--;
            if (arr[i] + arr[j] <= k)
                answer += j - i;
            else
                break;
        }

        System.out.println(answer);
    }
}