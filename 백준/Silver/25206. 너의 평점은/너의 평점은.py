import sys
import math
input = sys.stdin.readline

score = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

child = 0
parent = 0

for _ in range(20):
    sub, credit, grade = input().split()
    if grade == "P":
        continue

    s = score[grade]
    child += s * int(credit[:1])
    parent += int(credit[:1])

ans = round(child/parent, 6)
print(ans)