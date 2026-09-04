import java.util.*;

public class Main {
    static int n;
    static boolean[] visited;
    static ArrayList<Integer> selected = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        visited = new boolean[n + 1];

        backtrack(0);
        System.out.println(sb);

    }

    static void backtrack(int depth) {
        if (depth == n) {
            for (Integer i : selected) {
                sb.append(i).append(" ");
            }
            sb.append("\n");
        }

        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                selected.add(i);
                visited[i] = true;
                backtrack(depth + 1);
                visited[i] = false;
                selected.remove(selected.size() - 1);
            }
        }
    }
}
