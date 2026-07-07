import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<int[]> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            points.add(new int[] {x1, +1, i});
            points.add(new int[] {x2, -1, i});
        }

        points.sort(Comparator.comparingInt((int[] e) -> e[0]));

        HashSet<Integer> duplicated = new HashSet<>();

        int answer = 0;
        int minX = 0;
        int maxX = 0;
        for (int i = 0; i < 2 * n; i++) {
            int[] p = points.get(i);
            if (p[1] == 1) {
                if (duplicated.isEmpty())
                    minX = p[0];
                duplicated.add(p[2]);
            } else {
                duplicated.remove(p[2]);
                if (duplicated.isEmpty()) {
                    maxX = p[0];
                    answer += maxX - minX;
                }
            }
        }
        System.out.println(answer);
    }
}
