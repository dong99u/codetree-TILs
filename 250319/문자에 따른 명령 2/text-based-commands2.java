import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String orders = sc.nextLine();

		int[] dx = new int[] {1, 0, -1, 0};
		int[] dy = new int[] {0, -1, 0, 1};

		// 첫 시작은 북쪽을 보고 있음.
		int dirNum = 3;

		int currX = 0;
		int currY = 0;

		for (char c : orders.toCharArray()) {
			if (c == 'L') {
				dirNum = (dirNum + 3) % 4;
			} else if (c == 'R') {
				dirNum = (dirNum + 1) % 4;
			} else if (c == 'F') {
				currX += dx[dirNum];
				currY += dy[dirNum];
			}
		}

		System.out.println(currX + " " + currY);

	}
}