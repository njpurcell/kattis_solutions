k = int(input())
friend = input()
mine = input()
m = 0
n = len(friend)
for i in range(n):
    if friend[i] == mine[i]:
        m += 1
print(n-abs(m-k))