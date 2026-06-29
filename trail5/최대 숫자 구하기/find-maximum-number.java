import java.util.*;
import java.io.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    static TreeSet<Integer> treeSet;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        treeSet = IntStream.rangeClosed(1, m)
            .boxed()
            .collect(Collectors.toCollection(TreeSet::new));

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            treeSet.remove(Integer.parseInt(st.nextToken()));
            System.out.println(treeSet.last());
        }
    }


}

