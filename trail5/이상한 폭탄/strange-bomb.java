import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        HashMap<Integer, TreeSet<Integer>> indexes = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            if (indexes.containsKey(num)) {
                indexes.get(num).add(i);
            } else {
                TreeSet<Integer> treeSet = new TreeSet<>();
                treeSet.add(i);
                indexes.put(num, treeSet);
            }
        }

        int answer = -1;
        for (Map.Entry<Integer, TreeSet<Integer>> e : indexes.entrySet()) {
            int[] array = e.getValue().stream().mapToInt(elem -> elem).toArray();
            if (array.length < 2)
                continue;
            else {
                for (int i = 1; i < array.length; i++) {
                    if (array[i] - array[i - 1] <= k) {
                        answer = Math.max(answer, e.getKey());
                        break;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}