import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0) {
            String w = br.readLine().trim();
            int k = Integer.parseInt(br.readLine().trim());

            Map<Character, List<Integer>> charMap = new HashMap<>();

            for (int i = 0; i < w.length(); i++) {
                char ch = w.charAt(i);
                charMap.computeIfAbsent(ch, x -> new ArrayList<>()).add(i);
            }

            int minLen = Integer.MAX_VALUE;
            int maxLen = -1;

            for (char ch : charMap.keySet()) {
                List<Integer> idxList = charMap.get(ch);
                if (idxList.size() < k) continue;

                for (int i = 0; i <= idxList.size() - k; i++) {
                    int start = idxList.get(i);
                    int end = idxList.get(i+k-1);
                    int len = end - start + 1;

                    minLen = Math.min(minLen, len);
                    maxLen = Math.max(maxLen, len);
                }
            }

            if (maxLen == -1 || minLen == Integer.MAX_VALUE) {
                sb.append("-1\n");
            } else {
                sb.append(minLen).append(" ").append(maxLen).append("\n");
            }

        }
        System.out.print(sb);
    }
}