import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            String word = br.readLine();
            int len = word.length();

            System.out.println(word.charAt(0) + "" + word.charAt(len-1));
        }
    }
}
