def mario_time():
    n, y  = map(int, input().split())
    x = 0
    x_s = list()
    for _ in range(y):
        x_i = int(input())
        if x_i not in x_s:
            x_s.append(x_i)
            x += 1
    missed = [str(i) for i in range(n) if i not in x_s]
    print("\n".join(missed))
    print("Mario got " + str(x) + " of the dangerous obstacles.")

if __name__ == "__main__":
    mario_time()