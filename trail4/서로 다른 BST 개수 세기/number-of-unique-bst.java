import java.util.*;

public class Main {
    static int n;
    static int[] memo; // 메모이제이션

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        memo = new int[n + 1];
        Arrays.fill(memo, -1);

        int answer = backtrack(n);
        System.out.println(answer);
    }

    // label: 남은 노드의 개수
    static int backtrack(int count) {
        if (memo[count] != -1) {
            return memo[count];
        }
        if (count <= 1) {
            return 1;
        }
        int result = 0;
        for (int root = 1; root < count + 1; root++) {
            int left = backtrack(root - 1);
            int right = backtrack(count - root);
            result += left * right;
        }
        memo[count] = result;
        return memo[count];
    }
}
