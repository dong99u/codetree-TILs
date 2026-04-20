import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		HashSet<Integer> hashSet = new HashSet<>();

		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String order = st.nextToken();

			switch (order) {
				case "add":
					hashSet.add(Integer.parseInt(st.nextToken()));
					break;
				case "remove":
					hashSet.remove(Integer.parseInt(st.nextToken()));
					break;
				case "find":
					boolean result = hashSet.contains(Integer.parseInt(st.nextToken()));
					System.out.println(result);
					break;
			}
		}
	}
}
