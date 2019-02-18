def build_team():
    n, k = map(int, input().split())
    pokenom = dict()
    for i in range(1,n+1):
        pokenom[i] = list(map(int, input().split()))
    # Attack, Defense, Health
    max_values = [[0 for i in range(k)] for i in range(3)]
    max_pokes = [[0 for i in range(k)] for i in range(3)]    
    for nom, stats in pokenom.items():
        for i in range(3):
            min_idx = max_values[i].index(min(max_values[i]))
            if stats[i] > max_values[i][min_idx]:
                max_values[i][min_idx] = stats[i]
                # save a loop by tracking who the new max is
                max_pokes[i][min_idx] = nom
    s = set()
    for x in max_pokes:
        for i in range(k):
            s.add(x[i])
    print(len(s))

if __name__ == "__main__":
    build_team()