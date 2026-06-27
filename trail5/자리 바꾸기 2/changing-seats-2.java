import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            arr[i] = i;
        }

        HashSet<Integer>[] hashSets = new HashSet[n + 1];
        int[][] switches = new int[k][2];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            switches[i][0] = Integer.parseInt(st.nextToken());
            switches[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            hashSets[i] = new HashSet<>(Arrays.asList(i));
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < k; j++) {
                // a와 b 위치 바꾸기
                int a = switches[j][0];
                int b = switches[j][1];

                // swap
                int tmp = arr[a];
                arr[a] = arr[b];
                arr[b] = tmp;

                hashSets[arr[a]].add(a);
                hashSets[arr[b]].add(b);
            }
        }

        for (int i = 1; i <= n; i++) {
            System.out.println(hashSets[i].size());
        }

    }
}
