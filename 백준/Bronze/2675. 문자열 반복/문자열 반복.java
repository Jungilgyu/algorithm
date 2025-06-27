import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int number = Integer.parseInt(st.nextToken());
            String str = st.nextToken();

            StringBuilder answer = new StringBuilder();
            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                for (int j = 0; j < number; j++){
                    answer.append(ch);
                }
            }

            System.out.println(answer.toString());
        }

    }
}

