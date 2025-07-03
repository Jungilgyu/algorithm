import sys
input = sys.stdin.readline

p, m = map(int, input().split())
infos = []
for _ in range(p):
    l, n = input().split()
    infos.append([int(l), n])

# for x in infos:
#     print(x)

rooms = []

for l, n in infos:
    if len(rooms) == 0:
        new_room = []
        new_room.append([l, n])
        rooms.append(new_room)
    else:
        is_joined = False
        for i in range(len(rooms)):
            current_room = rooms[i]
            manager_level = current_room[0][0]

            if (abs(manager_level - l) <= 10) and len(current_room) < m:
                current_room.append([l, n])
                is_joined = True
                break
            else: # 다음방 검사
                continue
        if is_joined == False:
            new_room = []
            new_room.append([l, n])
            rooms.append(new_room)


for room in rooms:
    sorted_room = sorted(room, key=lambda x: x[1])
    if len(sorted_room) == m:
        print("Started!")
        for i in range(m):
            print(*sorted_room[i])
    else:
        print("Waiting!")
        for i in range(len(sorted_room)):
            print(*sorted_room[i])




