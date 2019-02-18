def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        prizes = dict()
        for j in range(n):
            line = input().split()
            line[0] = int(line[0])
            for k in range(line[0]):
                line[k+1] = int(line[k+1])
            prizes[j] = (line[1:line[0]+1], int("".join(line[line[0]+1:])))
        sticker_values = [0]
        # the index is the sticker number (leave 0 as empty string)
        sticker_values += map(int, input().split())
        total = 0
        for prize in prizes:
            min_value = 10000000
            for sticker in prizes[prize][0]:
                if sticker_values[sticker] < min_value:
                    min_value = sticker_values[sticker]
            total += min_value * prizes[prize][1]
        print(total)

if __name__ == "__main__":
    main()