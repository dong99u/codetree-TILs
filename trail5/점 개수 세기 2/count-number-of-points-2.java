import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][2];
        TreeSet<Integer> xSet = new TreeSet<>();
        TreeSet<Integer> ySet = new TreeSet<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr[i] = new int[] {x, y};
            xSet.add(x);
            ySet.add(y);
        }

        HashMap<Integer, Integer> xMapper = new HashMap<>();
        HashMap<Integer, Integer> yMapper = new HashMap<>();

        int xIndex = 1;
        for (Integer num : xSet) {
            xMapper.put(num, xIndex++);
        }

        int yIndex = 1;
        for (Integer num : ySet) {
            yMapper.put(num, yIndex++);
        }

        int[][] grid = new int[xIndex][yIndex];
        for (int[] point : arr) {
            grid[xMapper.get(point[0])][yMapper.get(point[1])] = 1;
        }

        int[][] prefixSum = new int[xIndex][yIndex];
        for (int i = 1; i < xIndex; i++) {
            for (int j = 1; j < yIndex; j++) {
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + grid[i][j];
            }
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            Integer xs = xSet.ceiling(x1);
            Integer xe = xSet.floor(x2);
            Integer ys = ySet.ceiling(y1);
            Integer ye = ySet.floor(y2);

            if (xs == null || xe == null || ys == null || ye == null) {
                sb.append(0).append("\n");
                continue;
            }

            int xsIdx = xMapper.get(xs);
            int xeIdx = xMapper.get(xe);
            int ysIdx = yMapper.get(ys);
            int yeIdx = yMapper.get(ye);

            if (xsIdx > xeIdx || ysIdx > yeIdx) {
                sb.append(0).append("\n");
                continue;
            }

            int result = prefixSum[xeIdx][yeIdx]
                    - prefixSum[xsIdx - 1][yeIdx]
                    - prefixSum[xeIdx][ysIdx - 1]
                    + prefixSum[xsIdx - 1][ysIdx - 1];

            sb.append(result).append("\n");
        }

        System.out.println(sb);
    }
}
