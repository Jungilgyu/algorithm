import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
     
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 여기부터 풀이 작성
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<>();

        while (n-- > 0) {
            String[] command = br.readLine().split(" ");
            switch (command[0]) {
                case "push_front":
                    deque.addFirst(Integer.parseInt(command[1]));
                    break;
                case "push_back":
                    deque.addLast(Integer.parseInt(command[1]));
                    break;
                case "pop_front":
                    System.out.println(deque.isEmpty() ? -1 : deque.pollFirst());
                    break;
                case "pop_back":
                    System.out.println(deque.isEmpty() ? -1 : deque.pollLast());
                    break;
                case "size":
                    System.out.println(deque.size());
                    break;
                case "empty":
                    System.out.println(deque.isEmpty() ? 1 : 0);
                    break;
                case "front":
                    System.out.println(deque.isEmpty() ? -1 : deque.peekFirst());
                    break;
                case "back":
                    System.out.println(deque.isEmpty() ? -1 : deque.peekLast());
                    break;
            }
        }
    }
}
