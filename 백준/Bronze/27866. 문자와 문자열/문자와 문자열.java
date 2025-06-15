import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] parts = br.readLine().split("");
        int n = Integer.parseInt(br.readLine());

        String[] arr = new String[parts.length];

        for (int i = 0; i < parts.length; i++) {
            arr[i] = parts[i];
        }

        System.out.println(arr[n-1]);

    }
}
