import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int m;
    static int[] fires;
    static int[] stations;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        fires = new int[n];
        stations = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            fires[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            stations[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(fires);
        Arrays.sort(stations);

        int answer = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j + 1 < m && getDist(i, j) > getDist(i, j + 1)) {
                j++;
            }
            answer = Math.max(answer, getDist(i, j));
        }
        System.out.println(answer);
    }

    static int getDist(int i, int j) {
        return Math.abs(fires[i] - stations[j]);
    }
}
