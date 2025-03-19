import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] ability = new int[6];
		for (int i = 0; i < 6; i++) {
			ability[i] = sc.nextInt();
		}

		int minDiff = Integer.MAX_VALUE;

		int sumAll = Arrays.stream(ability).sum();

		for (int i = 0; i < 4; i++) {
			for (int j = i + 1; j < 5; j++) {
				for (int k = j + 1; k < 6; k++) {
					int sum = ability[i] + ability[j] + ability[k];
					int another = sumAll - sum;

					minDiff = Math.min(minDiff, Math.abs(sum - another));

				}
			}
		}

		System.out.println(minDiff);

	}
}