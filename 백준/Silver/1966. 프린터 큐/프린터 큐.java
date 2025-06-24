import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            String[] nm = br.readLine().split(" ");
            int n = Integer.parseInt(nm[0]);
            int m = Integer.parseInt(nm[1]);

            String[] nums = br.readLine().split(" ");
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(nums[i]);
            }
            
            Deque<int[]> deque = new ArrayDeque<>();
            for (int i = 0; i < n; i++) {
                deque.add(new int[] { i, arr[i]});
            }

            int printOrder = 0;

            while (!deque.isEmpty()) {
                int[] front = deque.poll();
                boolean hasHigher = false;

                for (int[] doc : deque) {
                    if (doc[1] > front[1]) {
                        hasHigher = true;
                        break;
                    }
                }

                if (hasHigher) {
                    deque.addLast(front);
                } else {
                    printOrder++;
                    if (front[0] == m) {
                        System.out.println(printOrder);
                        break;
                    }
                }
            }
         }
    }
}