import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] inputString = br.readLine().toCharArray();

        LinkedHashMap<Character, Integer> hashMap = new LinkedHashMap<>();

        for (char c : inputString) {
            hashMap.merge(c, 1, Integer::sum);
        }

        Character c = hashMap.entrySet().stream().filter(e -> e.getValue() == 1)
            .map(e -> e.getKey())
            .findFirst()
            .orElse(null);

        System.out.println(c != null ? c : "None");
    }
}
