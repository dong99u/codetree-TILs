import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] A = new int[n];
        int[] B = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        boolean isPossible = true;
        int i = 0;
        for (int j = 0; j < m; j++) {
            while (i < n && A[i] != B[j])
                i++;
            if (i == n) {
                isPossible = false;
                break;
            } else {
                i++;
            }
        }

        System.out.println(isPossible == true ? "Yes" : "No");
    }
}