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
            points.add(new Point(x1, 1, i));
            points.add(new Point(x2, -1, i));
        }

        Collections.sort(points);

        HashSet<Integer> sets = new HashSet<>();

        int answer = 0;
        for (int i = 0; i < 2 * n; i++) {
            Point p = points.get(i);
            if (p.val == 1) {
                sets.add(p.index);
            } else {
                sets.remove(p.index);
                if (sets.isEmpty()) answer++;
            }
        }

        System.out.println(answer);
    }
}

class Point implements Comparable<Point> {
    int x;
    int val;
    int index;

    Point(int x, int val, int index) {
        this.x = x;
        this.val = val;
        this.index = index;
    }

    @Override
    public int compareTo(Point point) {
        return this.x - point.x;
    }
}