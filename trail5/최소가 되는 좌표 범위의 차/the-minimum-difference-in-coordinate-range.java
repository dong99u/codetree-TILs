import java.util.*;
import java.io.*;

public class Main {
    static final int MAX_VALUE = (int)1e6;

    static int n;
    static int d;

    static Point[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        arr = new Point[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[i] = new Point(x, y);
        }

        Arrays.sort(arr, Comparator.comparingInt((Point p) -> p.x)
            .thenComparingInt(p -> p.y));

        System.out.println(solution());

    }

    static int solution() {
        if (n == 1) {
            return -1;
        }

        TreeSet<Point> minMaxPoints = new TreeSet<>(Comparator.comparingInt((Point p) -> p.y)
            .thenComparingInt(p -> p.x));

        for (int i = 0; i < 2; i++) {
            minMaxPoints.add(arr[i]);
        }
        int j = 1;

        int answer = minMaxPoints.last().y - minMaxPoints.first().y >= d ? arr[1].x - arr[0].x : MAX_VALUE + 1;
        for (int i = 0; i < n - 1; i++) {
            while (j + 1 < n && minMaxPoints.last().y - minMaxPoints.first().y < d) {
                minMaxPoints.add(arr[j + 1]);
                j++;
            }
            if (minMaxPoints.last().y - minMaxPoints.first().y >= d)
                answer = Math.min(answer, arr[j].x - arr[i].x);
            minMaxPoints.remove(arr[i]);
            if (i + 1 == j && j + 1 < n) {
                minMaxPoints.add(arr[j + 1]);
                j++;
            }
        }

        return answer != MAX_VALUE + 1 ? answer : -1;
    }
}

class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

}
