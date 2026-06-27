import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[4][n];

        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 그룹 A, B / C, D 의 각각 숫자 조합을 모두 만들어놓기
        int[] firstArr = new int[n * n];
        for (int i = 0; i < n; i++) {
            int num1 = arr[0][i];
            for (int j = 0; j < n; j++) {
                int num2 = arr[1][j];
                firstArr[n * i + j] = num1 + num2;
            }
        }

        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int num1 = arr[2][i];
            for (int j = 0; j < n; j++) {
                int num2 = arr[3][j];
                hashMap.merge(num1 + num2, 1, Integer::sum);
            }
        }

        int answer = 0;
        for (int num : firstArr) {
            answer += hashMap.getOrDefault(-num, 0);
        }

        System.out.println(answer);
    }
}
