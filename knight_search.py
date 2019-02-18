def main():
    n = int(input())
    line = input()
    points = {
                'I':[],
                'C':[],
                'P':[],
                'A':[],
                'S':[],
                'G':[]
                }
    c = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if line[c] in points:
                points[line[c]].append([i,j])
            c += 1
    checks = ['IC','PC','AC','AS','AI','SG']
    for check in checks:
        match = False
        for p1 in points[check[0]]:
            for p2 in points[check[1]]:
                if ((p1[1] - p2[1])**2 + (p1[0] - p2[0])**2) == 5:
                    match = True
                    continue
        if not(match):
            break
    if match:
        print("YES")
    else:
        print("NO")

            
                
if __name__ == "__main__":
    main()

