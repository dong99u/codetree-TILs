import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] arr = new int[5];

		for (int i = 0; i < 5; i++) {
			arr[i] = sc.nextInt();
		}

		int answer = Integer.MAX_VALUE;

		// 첫 번째 그룹 선택 (2개)
		for (int i = 0; i < 5 - 1; i++) {
			for (int j = i + 1; j < 5; j++) {

				// 두 번째 그룹 선택 (2개)
				for (int k = 0; k < 5 - 1; k++) {
					if (k == i || k == j) continue;
					for (int l = k + 1; l < 5; l++) {
						if (l == i || l == j) continue;

						// 마지막 세 번째 그룹 선택 (1개)
						for (int m = 0; m < 5; m++) {
							if (m != i || m != j || m != k || m != l) {

								int[] scores = new int[3];

								scores[0] = arr[i] + arr[j];
								scores[1] = arr[k] + arr[l];
								scores[2] = arr[m];

								// 세 팀의 능력치가 모두 달라야 함
								if (scores[0] == scores[1] || scores[1] == scores[2] || scores[0] == scores[2]) {
									continue;
								}

								int maxVal = Arrays.stream(scores).max().getAsInt();
								int minVal = Arrays.stream(scores).min().getAsInt();

								answer = Math.min(answer, Math.abs(maxVal - minVal));

							}
						}
					}
				}
			}
		}

		System.out.println(answer);

	}
}