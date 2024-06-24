import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 정수 n 입력받기
        int n = scanner.nextInt();
        
        // n x n 크기의 2차원 배열 선언 및 값 입력받기
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        
        // solution 함수 호출 및 결과 출력
        int result = solution(n, matrix);
        System.out.println(result);
        
        scanner.close();
    }

    public static int solution(int n, int[][] matrix) {
        int maxCoinSum = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 2; j++) {
                int sumCoin = 0;
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        int x = i + k;
                        int y = j + l;
                        if (checkInRange(x, y, n)) {
                            sumCoin += matrix[x][y];
                        }
                    }
                }

                if (sumCoin > maxCoinSum) {
                    maxCoinSum = sumCoin;
                }
            }
        }
        
        
        return maxCoinSum;
    }

    

    public static boolean checkInRange(int x, int y, int n) {
        return x < n && y < n;
    }
}