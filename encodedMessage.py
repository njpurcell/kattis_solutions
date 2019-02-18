# 0.06 on kattis

def decode():
    for _ in range(int(input())):
        w = input()
        s = int(len(w)**(1/2))
        message = list()
        for i in range(s-1, -1, -1):
            for u in range(s):
                message.append(w[i + u * s])
        print("".join(message))

if __name__ == "__main__":
    decode()


# 0.21 on kattis

#def decode():
#    for _ in range(int(input())):
#        w = input()
#        s = int(len(w)**(1/2))
#        t = s - 1
#        while t > -1:
#            for u in range(s):
#                print(w[t + u * s], end="")
#            t -= 1
#        print("")
#
#
#if __name__ == "__main__":
#    decode()


# 0.26 on kattis

#def decode():
#    for _ in range(int(input())):
#        w = input()
#        s = int(len(w)**(1/2))
#        m = list()
#        idx = 0
#        for i in range(s):
#            m.append([])
#            for j in range(s):
#                m[i].append(w[idx])
#                idx += 1
#        for i in range(s):
#            for j in range(s):
#                print(m[j][-i-1], end="")
#        print("")