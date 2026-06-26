import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        HashMap<String, Integer> hashMapStringToInt = new HashMap<>();
        HashMap<Integer, String> hashMapIntToString = new HashMap<>();
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            String str = br.readLine();
            hashMapStringToInt.put(str, i);
            hashMapIntToString.put(i, str);
        }

        for (int i = 0; i < m; i++) {
            String str = br.readLine();
            if (str.chars().anyMatch(Character::isDigit)) {
                System.out.println(hashMapIntToString.get(Integer.parseInt(str)));
            } else {
                System.out.println(hashMapStringToInt.get(str));
            }
        }
    }
}