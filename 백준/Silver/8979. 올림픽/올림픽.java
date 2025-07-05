import java.io.*;
import java.util.*;

public class Main {
    static class Country implements Comparable<Country> {
        int number;
        int gold, silver, bronze;

        Country(int number, int gold, int silver, int bronze) {
            this.number = number;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }

        @Override
        public int compareTo(Country other){
            if (this.gold != other.gold) return other.gold - this.gold;
            if (this.silver != other.silver) return other.silver - this.silver;
            return other.bronze - this.bronze;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Country[] countries = new Country[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            countries[i] = new Country(number, g, s, b);
        }

        Arrays.sort(countries);

        int rank = 1;
        int[] prev = {countries[0].gold, countries[0].silver, countries[0].bronze};

        for (int i =0; i < n; i++) {
            Country c = countries[i];

            if (c.gold != prev[0] || c.silver != prev[1] || c.bronze != prev[2]) {
                rank = i + 1;
                prev[0] = c.gold;
                prev[1] = c.silver;
                prev[2] = c.bronze;
            }
            if (c.number == k) {
                System.out.println(rank);
                break;
            }
        }

    }
}