import java.io.*;
import java.util.*;

public class Main{
    static class Tower{
        int index;
        int height;

        Tower(int index, int height) {
            this.index = index;
            this.height = height;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] heights = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Tower> stack = new Stack<>();
        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {
            int currentHeight = heights[i];

            while (!stack.isEmpty() && stack.peek().height < currentHeight) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                answer[i] = stack.peek().index + 1;
            } else {
                answer[i] = 0;
            }

            stack.push(new Tower(i, currentHeight));
        }

        for (int i = 0; i < n; i++) {
            sb.append(answer[i]).append(' ');
        }
        System.out.println(sb);
    }
}