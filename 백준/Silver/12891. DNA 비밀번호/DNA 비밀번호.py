import sys
input = sys.stdin.readline

s, p = map(int, input().split())

dna = input().strip()
# A C G T 순

a, c, g, t = map(int, input().split())
mc = {'A':a, 'C':c, 'G':g, 'T':t}
cnt = {'A':0, 'C':0, 'G':0, 'T':0}

for i in range(p):
    cnt[dna[i]] += 1

def check():
    for ch in "ACGT":
        if cnt[ch] < mc[ch]:
            return False
    return True

ans = 0
if check():
    ans += 1

for i in range(p, s):
    cnt[dna[i]] += 1
    cnt[dna[i-p]] -= 1
    if check():
        ans += 1

print(ans)




