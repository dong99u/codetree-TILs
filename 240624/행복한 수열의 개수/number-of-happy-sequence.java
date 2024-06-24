import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        int answer = solution(n, m, matrix);

        System.out.println(answer);
        
    }

    public static int solution(int n, int m, int[][] matrix) {
        
        // 행 방향부터 
        int result = 0;
        for (int i = 0; i < n; i++) {
            int cnt = 1;
            for (int j = 1; j < n; j++) {
                if (matrix[i][j - 1] == matrix[i][j]) {
                    cnt++;
                } else {
                    cnt = 1;
                }
            }
            if (cnt >= m) {
                result++;
                break;
            }
        }
    
        for (int i = 0; i < n; i++) {
            int cnt = 1;
            for (int j = 1; j < n; j++) {

                if (matrix[j - 1][i] == matrix[j][i]) {
                    cnt++;
                } else {
                    cnt = 1;
                }

                
            }
            if (cnt >= m) {
                result++;
                break;
            }
        }

        
        return result;
    }


}