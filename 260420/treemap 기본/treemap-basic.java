import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		TreeMap<Integer, Integer> treeMap = new TreeMap<>();

		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String order = st.nextToken();

			int k, v;
			switch (order) {
				case "add":
					k = Integer.parseInt(st.nextToken());
					v = Integer.parseInt(st.nextToken());
					treeMap.put(k, v);
					break;

				case "remove":
					k = Integer.parseInt(st.nextToken());
					treeMap.remove(k);
					break;

				case "find":
					k = Integer.parseInt(st.nextToken());
					int result = treeMap.getOrDefault(k, -1);
					System.out.println(result != -1 ? result : "None");
					break;

				case "print_list":
					Iterator<Map.Entry<Integer, Integer>> it = treeMap.entrySet().iterator();
					if (treeMap.isEmpty()) {
						System.out.println("None");
						break;
					}
					while (it.hasNext()) {
						Map.Entry<Integer, Integer> next = it.next();
						System.out.print(next.getValue() + " ");
					}
					System.out.println();
					break;
			}
		}

	}
}
