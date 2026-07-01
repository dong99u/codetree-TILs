import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        long[][] people = new long[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            people[i][0] = Long.parseLong(st.nextToken());
            people[i][1] = Long.parseLong(st.nextToken());
        }

        int answer = 0;
        long threshold = Long.MAX_VALUE;

        for (int i = n - 1; i >= 0; i--) {
            long f = people[i][0] + people[i][1] * t;

            if (f >= threshold) {
                
            } else {
                answer++;
                threshold = f;
            }
        }

        System.out.println(answer);
    }
}