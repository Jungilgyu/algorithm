import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int dailyFeed = Integer.parseInt(br.readLine());

            String[] parts = br.readLine().split(" ");
            int[] feeds = new int[6];
            for (int i = 0; i < 6; i++) {
                feeds[i] = Integer.parseInt(parts[i]);
            }

            int sum = Arrays.stream(feeds).sum();
            if(sum > dailyFeed) {
                System.out.println(1);
            } else {
                int day_cnt = 2;
                while(true) {
                    int[] next_feeds = new int[6];
                    for (int i = 0; i < 6; i++) {
                        next_feeds[i] = feeds[i] + feeds[(i+5)%6] + feeds[(i + 1) % 6] + feeds[(i + 3) % 6];

                    }

                    int nextSum = Arrays.stream(next_feeds).sum();
                    if (nextSum <= dailyFeed) {
                        feeds = next_feeds;
                        day_cnt++;
                    } else {
                        System.out.println(day_cnt);
                        break;
                    }
                }
            }

        }
    }
}