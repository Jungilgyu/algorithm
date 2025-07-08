import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        String g = st.nextToken();
        
        Set<String> players = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String name = br.readLine();
            players.add(name);
        }
        
        int uniqueCount = players.size();
        
        if (g.equals("Y")) {
            System.out.println(uniqueCount);
        } else if (g.equals("F")) {
            System.out.println(uniqueCount / 2);
        } else {
            System.out.println(uniqueCount / 3);
        }
    }
}