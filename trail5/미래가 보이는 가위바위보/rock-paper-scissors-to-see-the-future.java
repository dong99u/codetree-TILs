import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        char[] arr = new char[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next().charAt(0);
        }

        int[][] P = new int[n][3]; // 가위, 바위, 보 순서
        int[][] L = new int[n][3];
        int[][] R = new int[n][3];
        for (int i = 0; i < n; i++) {
            P[i][0] = arr[i] == 'P' ? 1 : 0;
            P[i][1] = arr[i] == 'S' ? 1 : 0;
            P[i][2] = arr[i] == 'H' ? 1 : 0;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 0) L[i][j] = P[i][j];
                else L[i][j] = L[i - 1][j] + P[i][j];
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < 3; j++) {
                if (i == n - 1) R[i][j] = P[i][j];
                else R[i][j] = R[i + 1][j] + P[i][j];
            }
        }

        int answer = 0;

        // 한 번씩 바꿨을 때
        for (int i = 0; i < 3; i++) { // A가 처음 낸 것. ex) 가위
            for (int j = 0; j < 3; j++) { // A가 바꿀 것. ex) 주먹
                for (int k = 1; k < n; k++) {
                    answer = Math.max(answer, L[k - 1][i] + R[k][j]);
                }
            }
        }

        for (int i = 0; i < 3; i++) {
            answer = Math.max(answer, L[n - 1][i]);
        }

        System.out.println(answer);
    }
}
