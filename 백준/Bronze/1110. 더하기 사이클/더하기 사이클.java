import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int original = n;
        int count = 0;

        while (true) {
            int left = n / 10;         // 10의 자리
            int right = n % 10;        // 1의 자리
            int sum = left + right;    // 자리수 합

            n = (right * 10) + (sum % 10);
            count++;

            if (n == original) {
                break;
            }
        }

        System.out.println(count);
    }
}
