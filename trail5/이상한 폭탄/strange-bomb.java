import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] arr = new int[n];
        int[] R = new int[n];

        HashMap<Integer, Integer> indexes = new HashMap<>();

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = n - 1; i >= 0; i--) {
            if (!indexes.containsKey(arr[i])) {
                R[i] = -1;
            } else {
                R[i] = indexes.get(arr[i]);
            }
            indexes.put(arr[i], i);
        }
        int answer = -1;
        for (int i = 0; i < n; i++) {
            if (R[i] != -1 && R[i] - i <= k) {
                answer = Math.max(answer, arr[i]);
            }
        }
        System.out.println(answer);
    }
}