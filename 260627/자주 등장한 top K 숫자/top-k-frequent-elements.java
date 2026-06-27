import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        int n = sc.nextInt();
        int k = sc.nextInt();

        for (int i = 0; i < n; i++) {
            hashMap.merge(sc.nextInt(), 1, Integer::sum);
        }

        List<Map.Entry<Integer, Integer>> list = hashMap.entrySet().stream()
            .sorted(Comparator.comparingInt((Map.Entry<Integer, Integer> e) -> e.getValue())
                .reversed()
                .thenComparing(e -> e.getKey(), Comparator.reverseOrder()))
            .collect(Collectors.toList());
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            sb.append(list.get(i).getKey()).append(" ");
        }

        System.out.println(sb.toString());

    }
}
