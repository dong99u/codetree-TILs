import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<int[]> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            arr.add(new int[] {x1, 1});
            arr.add(new int[] {x2, -1});
        }

        arr.sort(Comparator.comparingInt(e -> e[0]));

        int answer = 0;
        int cur = 0;
        for (int i = 0; i < 2 * n; i++) {
            int[] elem = arr.get(i);

            cur += elem[1];
            answer = Math.max(answer, cur);
        }
        System.out.println(answer);
    }

}