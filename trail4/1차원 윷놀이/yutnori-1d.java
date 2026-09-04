import java.util.*;

public class Main {

    static int[] positions; // 말의 현재 위치

    static int n;
    static int m;
    static int k;
    static int[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();

        arr = new int[n]; // 말의 움직이는 크기
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        positions = new int[k];
        Arrays.fill(positions, 1);
        int answer = backtrack(0);
        System.out.println(answer);

    }

    static int backtrack(int depth) {
        if (depth == n) {
            int result = 0;
            for (int i = 0; i < k; i++) {
                if (positions[i] >= m)
                    result++;
            }
            return result;
        }

        int result = 0;
        for (int i = 0; i < k; i++) {
            positions[i] += arr[depth];
            result = Math.max(result, backtrack(depth + 1));
            positions[i] -= arr[depth];
        }
        return result;
    }
}
