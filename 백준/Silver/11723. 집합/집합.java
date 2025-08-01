import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int m = Integer.parseInt(br.readLine());
        Set<Integer> s = new HashSet<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int n = 0;

            if (st.hasMoreTokens()){
                n = Integer.parseInt(st.nextToken());
            }

            switch (cmd) {
                case "add":
                    s.add(n);
                    break;
                case "remove":
                    s.remove(n);
                    break;
                case "check":
                    sb.append(s.contains(n) ? 1 : 0).append('\n');
                    break;
                case "toggle":
                    if (s.contains(n)) {
                        s.remove(n);
                    } else {
                        s.add(n);
                    }
                    break;
                case "all":
                    s.clear();
                    for (int j = 1; j <= 20; j++) {
                        s.add(j);
                    }
                    break;
                case "empty":
                    s.clear();
                    break;
            }
        }
        System.out.println(sb);
    }
}