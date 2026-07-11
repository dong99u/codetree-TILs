import java.util.*;
import java.io.*;

public class Main {
    static final int MAX_IDX = (int)1e9 + 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Integer> treeSet = new TreeSet<>();
        int[] fires = new int[n];
        int[] stations = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            fires[i] = Integer.parseInt(st.nextToken());
            treeSet.add(fires[i]);
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            stations[i] = Integer.parseInt(st.nextToken());
            treeSet.add(stations[i]);
        }

        HashMap<Integer, Integer> mapper = new HashMap<>();
        int num = 0;
        for (Integer i : treeSet) {
            mapper.put(i, num);
            num++;
        }

        int[] L = new int[num];
        int[] R = new int[num];

        Arrays.fill(L, -MAX_IDX);
        Arrays.fill(R, MAX_IDX);

        for (int station : stations) {
            L[mapper.get(station)] = station;
            R[mapper.get(station)] = station;
        }

        for (int i = 1; i < num; i++) {
            L[i] = Math.max(L[i - 1], L[i]);
        }
        for (int i = num - 2; i >= 0; i--) {
            R[i] = Math.min(R[i + 1], R[i]);
        }

        int answer = 0;
        for (int fire : fires) {
            answer = Math.max(answer, Math.min(fire - L[mapper.get(fire)], R[mapper.get(fire)] - fire));
        }
        System.out.println(answer);
    }

}
