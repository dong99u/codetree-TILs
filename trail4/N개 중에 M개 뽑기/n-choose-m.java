import java.util.*;

public class Main {
    static int n;
    static int m;
    static ArrayList<Integer> selected = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        backtrack(1, 0);
        System.out.println(sb);
    }

    static void backtrack(int start, int depth) {
        if (depth == m) {
            for (Integer i : selected) {
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i <= n; i++) {
            selected.add(i);
            backtrack(i + 1, depth + 1);
            selected.remove(selected.size() - 1);
        }
    }
}
