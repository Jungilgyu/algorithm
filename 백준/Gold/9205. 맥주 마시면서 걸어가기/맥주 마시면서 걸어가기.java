import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static Point[] stores;
    static Point end;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T --> 0) {
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int startX = Integer.parseInt(st.nextToken());
            int startY = Integer.parseInt(st.nextToken());

            stores = new Point[n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                stores[i] = new Point(x, y);
            }

            st = new StringTokenizer(br.readLine());
            int endX = Integer.parseInt(st.nextToken());
            int endY = Integer.parseInt(st.nextToken());
            end = new Point(endX, endY);

            System.out.println(bfs(startX, startY));
        }

    }

    static String bfs(int sx, int sy) {
        Queue<Point> q = new LinkedList<>();
        boolean[] visited = new boolean[n];
        q.offer(new Point(sx, sy));

        while (!q.isEmpty()) {
            Point cur = q.poll();

            if (distance(cur, end) <= 1000) {
                return "happy";
            }

            for (int i = 0; i < n; i++) {
                if (!visited[i] && distance(cur, stores[i]) <= 1000) {
                    visited[i] = true;
                    q.offer(stores[i]);
                }
            }
        }

        return "sad";
    }

    static int distance(Point a, Point b) {
        return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    }

    static class Point {
        int x, y;
        Point(int x, int y) { this.x = x; this.y = y;}
    }

}