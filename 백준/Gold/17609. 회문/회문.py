import sys
input = sys.stdin.readline

def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

n = int(input())
for _ in range(n):
    word = input().strip()
    l, r = 0, len(word) - 1
    ans = 0  

    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            if is_palindrome(word, l+1, r) or is_palindrome(word, l, r-1):
                ans = 1
            else:
                ans = 2
            break  
    print(ans)
