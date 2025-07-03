import java.io.*;
import java.util.*;

public class Main {
    static class Player {
        int level;
        String name;
        Player(int level, String name) {
            this.level = level;
            this.name = name;
        }
    }

    static class Room {
        int leader;
        List<Player> players;
        Room(int leader, Player firstPlayer) {
            this.leader = leader;
            this.players = new ArrayList<>();
            this.players.add(firstPlayer);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Player> infos = new ArrayList<>();
        for (int i = 0; i < p; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            String n = st.nextToken();
            infos.add(new Player(l, n));
        }

        List<Room> rooms = new ArrayList<>();
        for (Player player: infos) {
            boolean isJoined = false;
            for (Room room : rooms) {
                if (Math.abs(room.leader - player.level) <= 10 && room.players.size() < m) {
                    room.players.add(player);
                    isJoined = true;
                    break;
                }
            }
            if (!isJoined) {
                rooms.add(new Room(player.level, player));
            }
        }

        StringBuilder sb = new StringBuilder();
        for (Room room : rooms) {
            List<Player> sortedPlayers = new ArrayList<>(room.players);
            sortedPlayers.sort(Comparator.comparing(ply -> ply.name));

            if (sortedPlayers.size() == m) {
                sb.append("Started!\n");
            } else {
                sb.append("Waiting!\n");
            }

            for (Player ply : sortedPlayers) {
                sb.append(ply.level).append(" ").append(ply.name).append("\n");
            }
        }

        System.out.print(sb);

    }
}