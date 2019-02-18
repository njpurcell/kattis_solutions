def optimize_costume():
    categories = dict()
    for _ in range(int(input())):
        stume = input()
        if stume not in categories:
            categories[stume] = 1
        else:
            categories[stume] += 1
    min_val = 1001    
    for val in categories.values():
        if val < min_val:
            min_val = val
    min_stumes = list()
    for stume, val in categories.items():
        if val == min_val:
            min_stumes.append(stume)
    min_stumes.sort()
    print("\n".join(min_stumes))

if __name__ == "__main__":
    optimize_costume()