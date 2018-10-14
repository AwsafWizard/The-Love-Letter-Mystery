
t = int(input())
letters = "abcdefghijklmnopqrstuvwxyz"

for x in range(t):

    s = input()
    ans = 0

    for a, b in zip(s, s[::-1]):

        if a > b and a != b:
            ans += letters.index(a) - letters.index(b)

    print(ans)