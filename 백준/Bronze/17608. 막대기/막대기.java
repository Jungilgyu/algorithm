import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[i] = num;
        }

        int cnt = 1;
        int temp = arr[n-1];
        for (int i = n-2; i >= 0; i--) {
            if (arr[i] > temp) {
                cnt += 1;
                temp = arr[i];
            }
        }

        System.out.println(cnt);



    }
}