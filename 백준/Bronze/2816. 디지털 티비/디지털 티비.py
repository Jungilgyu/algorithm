import sys

n = int(input())
ch = [input().strip() for _ in range(n)]

kbs1 = ch.index("KBS1")
print("1" * kbs1 + "4" * kbs1, end="")

kbs2 = ch.index("KBS2")
if kbs2 < kbs1:
    kbs2 += 1

print("1" * kbs2 + "4" * (kbs2 - 1))