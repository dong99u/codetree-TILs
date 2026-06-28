import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        TreeSet<Point> treeSet = new TreeSet<>(
            Comparator.comparing(Point::getX)
                .thenComparing(Point::getY)
        );

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            treeSet.add(new Point(x, y));
        }

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            NavigableSet<Point> points = treeSet.tailSet(new Point(x, y), true);

            if (points.isEmpty()) {
                System.out.println(-1 + " " + -1);
                continue;
            }

            Point result = points.first();
            System.out.println(result.getX() + " " + result.getY());

        }
    }

}

class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    void setX(int x) {
        this.x = x;
    }

    void setY(int y) {
        this.y = y;
    }

    int getX() {
        return this.x;
    }

    int getY() {
        return this.y;
    }
}