import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Node cur = new Node(br.readLine());

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "1": {
                    Node newNode = new Node(st.nextToken());
                    if (cur.prev == null) {
                        cur.prev = newNode;
                        newNode.next = cur;
                    } else {
                        Node prev = cur.prev;
                        prev.next = newNode;
                        newNode.prev = prev;
                        newNode.next = cur;
                        cur.prev = newNode;
                    }
                    break;
                }
                case "2": {
                    Node newNode = new Node(st.nextToken());
                    if (cur.next == null) {
                        cur.next = newNode;
                        newNode.prev = cur;
                    } else {
                        Node next = cur.next;
                        next.prev = newNode;
                        newNode.next = next;
                        newNode.prev = cur;
                        cur.next = newNode;
                    }
                    break;
                }
                case "3": {
                    cur = cur.prev != null ? cur.prev : cur;
                    break;
                }
                case "4": {
                    cur = cur.next != null ? cur.next : cur;
                    break;
                }
            }
            addResult(sb, cur);
        }
        System.out.println(sb);
    }

    static void addResult(StringBuilder sb, Node cur) {
        if (cur.prev == null) {
            sb.append("(Null)").append(" ");
        } else {
            sb.append(cur.prev.value).append(" ");
        }

        sb.append(cur.value).append(" ");

        if (cur.next == null) {
            sb.append("(Null)").append(" ");
        } else {
            sb.append(cur.next.value).append(" ");
        }
        sb.append("\n");
    }

    static class Node {
        String value;
        Node prev;
        Node next;

        Node(String value) {
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }
}