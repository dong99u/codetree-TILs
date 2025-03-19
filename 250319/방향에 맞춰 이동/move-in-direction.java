import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int iterCount = Integer.parseInt(sc.nextLine());


		int[] dx = new int[] {1, 0, -1, 0};
		int[] dy = new int[] {0, -1, 0, 1};
		int dirNum = 0;

		int x = 0, y = 0;

		for (int i = 0; i < iterCount; i++) {

			String[] line = sc.nextLine().split(" ");

			if (line[0].equals("E")) {
				dirNum = 0;
			} else if (line[0].equals("S")) {
				dirNum = 1;
			} else if (line[0].equals("W")) {
				dirNum = 2;
			} else if (line[0].equals("N")) {
				dirNum = 3;
			}

			int quan = Integer.parseInt(line[1]);

			x += dx[dirNum] * quan;
			y += dy[dirNum] * quan;

		}

		System.out.println(x + " " + y);


	}
}