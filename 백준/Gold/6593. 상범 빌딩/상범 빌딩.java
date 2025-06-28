import java.io.*;
import java.util.*;

public class Main {

    static int L, R, C;
    static char[][][] building;
    static boolean[][][] visited;
    static int[] dx = {0, 1, 0, -1, 0, 0};  // 동, 남, 서, 북, 상, 하
    static int[] dy = {1, 0, -1, 0, 0, 0};
    static int[] dz = {0, 0, 0, 0, 1, -1};  // 층 이동은 z축

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());

            if (L == 0 && R == 0 && C == 0) break;

            building = new char[L][R][C];
            visited = new boolean[L][R][C];

            int startZ = 0, startX = 0, startY = 0;

            for (int l = 0; l < L; l++) {
                for (int r = 0; r < R; r++) {
                    String line = br.readLine();
                    for (int c = 0; c < C; c++) {
                        building[l][r][c] = line.charAt(c);
                        if (building[l][r][c] == 'S') {
                            startZ = l;
                            startX = r;
                            startY = c;
                        }
                    }
                }
                br.readLine(); // 빈 줄 처리
            }

            int result = bfs(startZ, startX, startY);
            if (result == -1) {
                System.out.println("Trapped!");
            } else {
                System.out.println("Escaped in " + result + " minute(s).");
            }
        }
    }

    static int bfs(int z, int x, int y) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{z, x, y, 0});
        visited[z][x][y] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cz = cur[0], cx = cur[1], cy = cur[2], time = cur[3];

            if (building[cz][cx][cy] == 'E') return time;

            for (int i = 0; i < 6; i++) {
                int nz = cz + dz[i];
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (0 <= nz && nz < L && 0 <= nx && nx < R && 0 <= ny && ny < C) {
                    if (!visited[nz][nx][ny] && building[nz][nx][ny] != '#') {
                        visited[nz][nx][ny] = true;
                        queue.add(new int[]{nz, nx, ny, time + 1});
                    }
                }
            }
        }

        return -1;
    }
}
