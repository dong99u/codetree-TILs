import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] chars = br.readLine().toCharArray();
        int n = chars.length;

        int[] arr = new int['z' - 'a' + 1];
        int answer = 0;
        int j = -1;
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && arr[chars[j + 1] - 'a'] < 1) {
                arr[chars[j + 1] - 'a']++;
                j++;
            }
            answer = Math.max(answer, j - i + 1);
            arr[chars[i] - 'a']--;
        }
        System.out.println(answer);
    }
}
