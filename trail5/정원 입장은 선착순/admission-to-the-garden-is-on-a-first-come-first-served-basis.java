import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 더미 없이 0-based로 채우되, 번호(축2)는 1-based로 저장
        int[][] people = new int[n][3];
        for (int i = 0; i < n; i++) {
            int arrivedAt = sc.nextInt();
            int stayTime  = sc.nextInt();
            people[i] = new int[] { arrivedAt, i + 1, stayTime }; // 도착, 번호, 머무름
        }

        // 축1: 도착 시간 순 (오프라인이므로 딱 한 번만 정렬)
        Arrays.sort(people, Comparator.comparingInt((int[] p) -> p[0]));

        // 아직 안 온 사람: 정렬된 순서로 앞에서 소비만 → ArrayDeque
        ArrayDeque<int[]> notArrived =
            Arrays.stream(people).collect(Collectors.toCollection(ArrayDeque::new));

        // 축2: 이미 도착해 기다리는 사람 = 번호 오름차순 min-heap
        PriorityQueue<int[]> waiting =
            new PriorityQueue<>(Comparator.comparingInt((int[] p) -> p[1]));

        long endTime = 0;       // 정원이 비는 시각
        long maxWaiting = 0;

        while (!notArrived.isEmpty() || !waiting.isEmpty()) {
            // 1) endTime까지 도착한 사람 "전원"을 대기열로 이동
            while (!notArrived.isEmpty() && notArrived.peekFirst()[0] <= endTime) {
                waiting.offer(notArrived.pollFirst());
            }

            // 2) 유휴 구간: 대기자가 없으면 다음 도착자 시각으로 점프만 하고 재루프
            if (waiting.isEmpty()) {
                endTime = notArrived.peekFirst()[0];
                continue; // 위로 올라가 그 시각 도착자를 1)에서 전부 넣는다
            }

            // 3) 번호가 가장 작은 사람 입장
            int[] cur = waiting.poll();
            maxWaiting = Math.max(maxWaiting, endTime - cur[0]);
            endTime += cur[2];
        }

        System.out.println(maxWaiting);
    }
}