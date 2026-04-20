import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		HashMap<Integer, Integer> hashMap = new HashMap<>();

		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String order = st.nextToken();

			int k;
			int v;
			switch (order) {
				case "add":
					k = Integer.parseInt(st.nextToken());
					v = Integer.parseInt(st.nextToken());
					hashMap.put(k, v);
					break;

				case "remove":
					k = Integer.parseInt(st.nextToken());
					hashMap.remove(k);
					break;
				case "find":
					k = Integer.parseInt(st.nextToken());
					Integer result = hashMap.getOrDefault(k, -1);

					System.out.println(result != -1 ? result : "None");
				
			}
		}

	}
}
