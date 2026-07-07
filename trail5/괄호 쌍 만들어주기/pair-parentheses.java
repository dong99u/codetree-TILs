import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] chars = br.readLine().toCharArray();
        int n = chars.length;

        int[] L = new int[n];
        ArrayList<Integer> closes = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            L[i] = L[i - 1] + (chars[i - 1] == chars[i] && chars[i] == '(' ? 1 : 0);
        }

        long answer = 0;
        for (int i = 1; i < n; i++) {
            if (chars[i] == ')' && chars[i - 1] == chars[i]) {
                answer += L[i - 1];
            }
        }
        System.out.println(answer);

    }
}
