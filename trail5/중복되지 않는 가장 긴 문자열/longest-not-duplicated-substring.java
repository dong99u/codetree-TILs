import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] chars = br.readLine().toCharArray();
        int n = chars.length;

        char c = 'a';
        int[] arr = new int['z' - 'a' + 1];
        arr[chars[0] - 'a']++;
        int answer = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && arr[chars[j] - 'a'] <= 1) {
                arr[chars[j + 1] - 'a']++;
                j++;
            }
            if (arr[chars[i] - 'a'] <= 1) {
                if (arr[chars[j] - 'a'] > 1)
                    answer = Math.max(answer, j - i);
                else if (j == n - 1)
                    answer = Math.max(answer, j - i + 1);
            }
            arr[chars[i] - 'a']--;
        }

        System.out.println(answer);
    }
}
