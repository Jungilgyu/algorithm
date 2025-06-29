import java.io.*;
import java.util.*;

public class Main {

    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int getDistance(Point a, Point b) {
        return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Point[] checkPoints = new Point[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            checkPoints[i] = new Point(x, y); // 여기
        }

        int total = 0;
        for (int i = 0; i < n-1; i ++) {
            total += getDistance(checkPoints[i], checkPoints[i+1]);
        }

        int minDistance = Integer.MAX_VALUE;

        for (int i = 1; i < n-1; i++) {
            int original = getDistance(checkPoints[i - 1], checkPoints[i]) +
                    getDistance(checkPoints[i], checkPoints[i + 1]);
            int shortcut = getDistance(checkPoints[i - 1], checkPoints[i + 1]);
            int newTotal = total - original + shortcut;

            minDistance = Math.min(minDistance, newTotal);
        }

        System.out.println(minDistance);

    }
}