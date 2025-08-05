import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[][] area;
    static boolean[][] visited;
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        area = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                area[i][j] = line.charAt(j) - '0';
            }
        }

        int ans = 0;
        for (int h = 2; h <= 9; h++) {
            visited = new boolean[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (area[i][j] < h && !visited[i][j]) {
                        int temp = bfs(i, j, h);
                        if (temp != -1) {
                            ans += temp;
                        }
                    }
                }
            }
        }

        System.out.println(ans);
    }

    static int bfs(int i, int j, int h) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {i, j});
        visited[i][j] = true;

        List<int[]> conn = new ArrayList<>();
        conn.add(new int[] {i, j});

        boolean adjOutline = false;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            for (int d = 0; d < 4; d++) {
                int nx = x + di[d];
                int ny = y + dj[d];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (!visited[nx][ny] && area[nx][ny] < h) {
                        q.add(new int[] {nx, ny});
                        visited[nx][ny] = true;
                        conn.add(new int[] {nx, ny});
                    }
                } else {
                    adjOutline = true;
                }
            }
        }

        if (adjOutline) {
            return -1;
        }

        int res = 0;
        for (int[] p : conn) {
            int x = p[0], y = p[1];
            res += h - area[x][y];
            area[x][y] = h;
        }

        return res;
    }
}