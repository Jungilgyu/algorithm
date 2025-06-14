import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
     
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];

        String[] parts = br.readLine().split(" ");

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(parts[i]);
        }

        int max_num = Arrays.stream(nums).max().getAsInt();

        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += ((double) nums[i] / max_num) * 100;
        }

        double answer = sum / n;
        System.out.println(answer);
    }
}
