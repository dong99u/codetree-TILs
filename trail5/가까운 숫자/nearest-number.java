import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        TreeSet<Integer> treeSet = new TreeSet<>(Arrays.asList(0));

        int minDistance = Integer.MAX_VALUE;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int val = Integer.parseInt(st.nextToken());

            Integer right = treeSet.higher(val);
            Integer left = treeSet.lower(val);

            if (left != null && right != null)
                minDistance = Math.min(minDistance, Math.min(Math.abs(val - left), Math.abs(right - val)));
            else if (left == null)
                minDistance = Math.min(minDistance, Math.abs(right - val));
            else
                minDistance = Math.min(minDistance, Math.abs(val - left));

            treeSet.add(val);

            System.out.println(minDistance);
        }
    }


}
