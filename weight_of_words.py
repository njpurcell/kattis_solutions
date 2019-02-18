#def calc_weight(word):
#    weight = 0
#    for char in word:
#        weight += ord(char) - 96
#    return weight

def wow():
    l, w = map(int, input().split())
    s = list("a" * l)
    k = l
    if l * 26 < w or l > w:
        print("impossible")
    elif k == w:
        print(''.join(s))
    else: 
        for i in range(l):
            val = 97
            idx = l - 1 - i
            while val < 122:
                val += 1
                k += 1
                s[idx] = chr(val)
                if k == w:
                    print(''.join(s))
                    break
if __name__ == "__main__":
    wow()
    
#def wow():
#    l, w = map(int, tuple(input().split()))
#    if l * 26 < w or l > w:
#        #print("impossible")
#        print("", end="")
#    else:
#        c = int(w/l)
#        r = w - (c * (l-1))
#        if r < 27:
#            s = chr(96 + c) * (l - 1)
#            s += chr(96 + r)
#        else:
#            s = "z" * (l - 2)
#            r =  w - (26 * (l - 2))
#            if r > 26:
#                s += "z"
#                r -= 26
#                s += chr(96 + r)
#            else:
#                s += chr(96 + r - 1) + "a"
#        print(s)
