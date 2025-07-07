import sys

while True:
    p = input()
    if p == "end":
        break

    vowel = ['a', 'e', 'i', 'o', 'u']
    vowel_cnt = 0
    continuous_vowel = 0
    continuous_consonant = 0
    prev = ""
    res = True
    for i in range(len(p)):
        # 1번조건
        if p[i] in vowel:
            vowel_cnt += 1
        # 2번조건, 모음or 자음3개 연속 x
        if (prev in vowel) and (p[i] in vowel):
            continuous_vowel += 1
            if continuous_vowel >= 3:
                break
        elif (prev not in vowel) and (p[i] not in vowel):
            continuous_consonant += 1
            if continuous_consonant >= 3:
                break
        elif (prev in vowel) and (p[i] not in vowel):
            continuous_consonant = 1
        elif (prev not in vowel) and (p[i] in vowel):
            continuous_vowel = 1


        if prev == p[i]:
            if (p[i] == 'e') or (p[i] == 'o'):
                continue
            else:
                res = False

        prev = p[i]
    if vowel_cnt == 0:
        res = False

    if continuous_vowel >= 3 or continuous_consonant >= 3:
        res = False
    # print(vowel_cnt)
    # print(continuous_vowel)
    # print(continuous_consonant)
    # print(prev)
    # print(res)
    if res == True:
        print(f"<{p}> is acceptable.")
    else:
        print(f"<{p}> is not acceptable.")




