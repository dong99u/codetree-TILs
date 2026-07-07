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
            points.add(new Point(x1, +1));
            points.add(new Point(x2, -1));
        }

        Collections.sort(points);

        int answer = 0;
        int curCount = 0;

        for (int i = 0; i < 2 * n; i++) {
            Point p = points.get(i);
            curCount += p.val;
            answer = Math.max(answer, curCount);
        }
        System.out.println(answer);
    }
}

class Point implements Comparable<Point> {
    int x;
    int val;

    Point(int x, int val) {
        this.x = x;
        this.val = val;
    }

    @Override
    public int compareTo(Point point) {
        return this.x - point.x;
    }
}