import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int M = Integer.parseInt(br.readLine());

            PriorityQueue<Integer> lowerMaxHeap = new PriorityQueue<>(Comparator.reverseOrder());
            PriorityQueue<Integer> upperMinHeap = new PriorityQueue<>();

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                int x = Integer.parseInt(st.nextToken());

                // 중앙값 구하기 로직
                if (lowerMaxHeap.isEmpty() || x <= lowerMaxHeap.peek())
                    lowerMaxHeap.offer(x);
                else
                    upperMinHeap.offer(x);

                // 크기 조정
                if (lowerMaxHeap.size() > upperMinHeap.size() + 1) 
                    upperMinHeap.offer(lowerMaxHeap.poll());
                else if (upperMinHeap.size() > lowerMaxHeap.size()) 
                    lowerMaxHeap.offer(upperMinHeap.poll());

                if (i % 2 == 0) { // 홀수  번째 수 마다 출력
                    sb.append(lowerMaxHeap.peek()).append(" ");
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}

