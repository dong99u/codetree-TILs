import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        sc.nextLine();

        String[] A = new String[n];
        String[] B = new String[n];

        for (int i = 0; i < n; i++) {
            A[i] = sc.nextLine();
        }

        for (int i = 0; i < n; i++) {
            B[i] = sc.nextLine();
        }

        int answer = 0;
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < m; j++) {
                for (int k = j + 1; k < m; k++) {
                    if (isDisjoint(A, B, i, j, k, n))
                        answer++;
                }
            }
        }
        System.out.println(answer);
    }

    static boolean isDisjoint(String[] A, String[] B, int a, int b, int c, int n) {
        HashSet<String> setA = new HashSet<>();
        HashSet<String> setB = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String stringA = String.valueOf(A[i].charAt(a)) + A[i].charAt(b) + A[i].charAt(c);
            setA.add(stringA);
            String stringB = String.valueOf(B[i].charAt(a)) + B[i].charAt(b) + B[i].charAt(c);
            setB.add(stringB);
        }

        return Collections.disjoint(setA, setB);
    }
}
