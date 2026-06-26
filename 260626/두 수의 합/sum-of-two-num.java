import java.util.*;

public class Main {
    public static void main(String[] args) {

        HashMap<Integer, Integer> hashMap = new HashMap<>();

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            arr[i] = num;
            hashMap.put(num, hashMap.getOrDefault(num, 0) + 1);
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            int num = arr[i];
            hashMap.put(num, hashMap.get(num) - 1);
            int target = k - num;

            if (hashMap.containsKey(target))
                answer += hashMap.get(target);

            hashMap.put(num, hashMap.get(num) + 1);
        }
        System.out.println(answer / 2);
        
    }
}