import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Set<String> S = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String x = br.readLine();
            S.add(x);
        }

        int cnt = 0;
        for (int i = 0; i < m; i++){
            String x = br.readLine();
            if (S.contains(x)) {
                cnt += 1;
            }
        }

        System.out.println(cnt);
    }
}