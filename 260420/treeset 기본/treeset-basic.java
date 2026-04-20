import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		TreeSet<Integer> treeSet = new TreeSet<>();

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String order = st.nextToken();

			switch (order) {
				case "add":
					treeSet.add(Integer.parseInt(st.nextToken()));
					break;

				case "remove":
					treeSet.remove(Integer.parseInt(st.nextToken()));
					break;

				case "find":
					System.out.println(treeSet.contains(Integer.parseInt(st.nextToken())));
					break;

				case "lower_bound":
					Integer ceiling = treeSet.ceiling(Integer.parseInt(st.nextToken()));
					if (ceiling == null) {
						System.out.println("None");
					} else {
						System.out.println(ceiling);
					}
					break;

				case "upper_bound":
					Integer higher = treeSet.higher(Integer.parseInt(st.nextToken()));
					if (higher == null) {
						System.out.println("None");
					} else {
						System.out.println(higher);
					}
					break;

				case "largest":
					if (treeSet.isEmpty()) {
						System.out.println("None");
						break;
					}
					System.out.println(treeSet.last());
					break;

				case "smallest":
					if (treeSet.isEmpty()) {
						System.out.println("None");
						break;
					}
					System.out.println(treeSet.first());
					break;
			}
		}
	}
}
