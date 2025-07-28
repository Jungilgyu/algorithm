import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int[] belt;
    static boolean[] robots;
    static int zeroCount = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer((br.readLine()));

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        belt = new int[2 * N];
        robots = new boolean[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 2 * N; i++) {
            belt[i] = Integer.parseInt(st.nextToken());
        }

        int step = 1;
        while (true) {
            rotateBelt();
            moveRobots();
            putRobots();

            if (zeroCount >= K) break;
            step++;
        }

        System.out.println(step);
    }

    static void rotateBelt() {
        int lastDurability = belt[2 * N - 1];
        for (int i = 2 * N - 1; i > 0; i--){
            belt[i] = belt[i - 1];
        }
        belt[0] = lastDurability;

        for (int i = N - 1; i > 0; i--) {
            robots[i] = robots[i-1];
        }
        robots[0] = false;
        robots[N-1] = false;
    }
    
    static void moveRobots() {
        for (int i = N - 2; i>= 0; i--) {
            if (robots[i] && !robots[i+1] && belt[i+1] > 0) {
                robots[i] = false;
                robots[i+1] = true;
                belt[i+1]--;
                if(belt[i+1] == 0) zeroCount++;
            }
        }
        robots[N-1] = false;
    }
    
    static void putRobots() {
        if (belt[0] > 0) {
            robots[0] = true;
            belt[0]--;
            if (belt[0] == 0) zeroCount++;
        }
    }
}