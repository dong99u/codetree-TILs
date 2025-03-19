import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		int answer = 0;
		for (int i = 1; i <= n; i++) { // 첫번째 자리
			for (int j = 1; j <= n; j++) { // 두번째 자리
				for (int k = 1; k <= n; k++) { // 세번째 자리
					if (isGood(i, j, k, a, b, c)) {
						answer++;
					}
				}
			}
		}

		System.out.println(answer);
	}

	private static boolean isGood(int i, int j, int k, int a, int b, int c) {
		if (Math.abs(a - i) <= 2 || Math.abs(b - j) <= 2 || Math.abs(c - k) <= 2) {
			return true;
		}

		return false;
	}
}