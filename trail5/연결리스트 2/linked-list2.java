import java.util.Scanner;

public class Main {
    // 최대 노드 개수
    public static final int MAX_N = 100005;

    // 한 노드를 나타내는 클래스입니다.
    static class Node {
        int id;
        Node prev, next;

        public Node(int id) {
            this.id = id;
            this.prev = null;
            this.next = null;
        }
    }

    public static Node[] nodes = new Node[MAX_N];

    // u 앞에 singleton을 삽입합니다.
    public static void insertPrev(Node u, Node singleton) {
        singleton.prev = u.prev;
        singleton.next = u;

        if (null != singleton.prev)
            singleton.prev.next = singleton;
        if (null != singleton.next)
            singleton.next.prev = singleton;
    }

    // u 뒤에 singleton을 삽입합니다.
    public static void insertNext(Node u, Node singleton) {
        singleton.prev = u;
        singleton.next = u.next;

        if (null != singleton.prev)
            singleton.prev.next = singleton;
        if (null != singleton.next)
            singleton.next.prev = singleton;
    }

    // 노드 u를 제거합니다.
    public static void pop(Node u) {
        if (u.prev != null)
            u.prev.next = u.next;

        if (u.next != null)
            u.next.prev = u.prev;

        u.prev = u.next = null;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();

        // N 개의 단일 노드를 생성합니다.
        for (int i = 1; i <= n; i++) {
            nodes[i] = new Node(i);
        }

        // Q 개의 연산을 진행합니다.
        for (int t = 0; t < q; t++) {
            int type = sc.nextInt();
            int i = sc.nextInt();

            if (1 == type) {
                pop(nodes[i]);
            } else if (2 == type) {
                int j = sc.nextInt();
                insertPrev(nodes[i], nodes[j]);
            } else if (3 == type) {
                int j = sc.nextInt();
                insertNext(nodes[i], nodes[j]);
            } else if (4 == type) {
                System.out.print((nodes[i].prev == null ? 0 : nodes[i].prev.id) + " ");
                System.out.println(nodes[i].next == null ? 0 : nodes[i].next.id);
            }
        }

        // 연산을 마친 후 1번 부터 N번 노드까지의 다음 노드 번호를 차례대로 한 줄에 출력합니다.
        for (int i = 1; i <= n; i++)
            System.out.print((nodes[i].next == null ? 0 : nodes[i].next.id) + " ");
        sc.close();
    }
}
