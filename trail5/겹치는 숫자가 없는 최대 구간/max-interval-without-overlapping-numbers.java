import java.util.*;
import java.io.*;

public class Main {
    static final int MAX_NUM = 100000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        int[] counts = new int[MAX_NUM + 1];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        counts[arr[0]] = 1;

        int answer = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && counts[arr[j + 1]] == 0) {
                counts[arr[j + 1]]++;
                j++;
            }
            answer = Math.max(answer, j - i + 1);
            counts[arr[i]]--;
        }

        System.out.println(answer);
    }
}
