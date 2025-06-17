import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine();
        int[] arr = new int[26];


        for (int i = 0; i < 26; i++) {
            arr[i] = -1;
        }

        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int index = ch - 'a';

            if (arr[index] == -1) {
                arr[index] = i;
            }
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(arr[i] + " ");
        }


    }
}
