import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<Point> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            points.add(new Point(x1, +1, i));
            points.add(new Point(x2, -1, i));
        }
        int answer = 0;
        Collections.sort(points);

        HashSet<Integer> dup = new HashSet<>();

        int minX = 0;
        int maxX = 0;
        for (int i = 0; i < 2 * n; i++) {
            Point point = points.get(i);

            if (point.val == 1) {
                if (dup.isEmpty()) {
                    minX = point.x;
                }
                dup.add(point.idx);
            } else {
                dup.remove(point.idx);
                if (dup.isEmpty()) {
                    maxX = point.x;
                    answer = Math.max(answer, maxX - minX);
                }
            }
        }

        System.out.println(answer);
    }
}

class Point implements Comparable<Point> {
    int x;
    int val;
    int idx;

    Point(int x, int val, int idx) {
        this.x = x;
        this.val = val;
        this.idx = idx;
    }

    @Override
    public int compareTo(Point point) {
        return this.x - point.x;
    }
}