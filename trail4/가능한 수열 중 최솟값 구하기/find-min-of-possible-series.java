import java.io.*;

public class Main {
    static int n;
    static int[] selected;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine().trim());
        selected = new int[n];

        backtrack(0);   // 첫 완성 수열이 곧 사전순 최소

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++)
            sb.append(selected[i]);
        System.out.println(sb);
    }

    // 완성(사전순 최소 발견)했으면 true를 반환해 위로 전파 → 즉시 탐색 종료
    static boolean backtrack(int depth) {
        if (depth == n)
            return true;          // ① 종료 조건

        for (int num = 4; num <= 6; num++) {  // ② 작은 수부터 시도 = 사전순 보장
            selected[depth] = num;
            if (isValid(depth)) {             // ③ 방금 놓은 칸 기준으로만 검사
                if (backtrack(depth + 1))
                    return true;
            }
            selected[depth] = 0;
        }
        return false;
    }

    /**
     * selected[0..lastIdx]가 유효한지 검사.
     * lastIdx를 오른쪽 끝으로 하는 "인접한 두 블록"만 보면 충분하다.
     */
    static boolean isValid(int lastIdx) {
        int len = lastIdx + 1;                       // 현재 채워진 길이

        for (int L = 1; L <= len / 2; L++) {         // 블록 길이 L
            int start2 = lastIdx - L + 1;            // 뒤 블록 시작
            int start1 = start2 - L;                 // 앞 블록 시작

            boolean same = true;
            for (int k = 0; k < L; k++) {
                if (selected[start1 + k] != selected[start2 + k]) {
                    same = false;
                    break;
                }
            }
            if (same)
                return false;                  // 인접 반복 발견 → 불가능
        }
        return true;
    }
}