import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int p = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < p; tc ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());

            int[] children = new int[20];
            for(int i = 0; i < 20; i++) {
                children[i] = Integer.parseInt(st.nextToken());
            }

            List<Integer> res = new ArrayList<>();
            res.add(children[0]);
            int cnt = 0;
            for (int i = 1; i < 20; i++) {
                res.add(children[i]);
                for (int j=0; j< i; j++) {
                    if (children[j] > children[i]) {
                        res.remove(i);
                        res.add(j, children[i]);
                        cnt++;
                   
                    }
                }
            }
            System.out.println(t + " " + cnt);

        }
    }
}