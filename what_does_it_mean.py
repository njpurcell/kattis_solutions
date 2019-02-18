from operator import mul
from functools import reduce

def prod(iterable):
    return reduce(mul, iterable, 1)

def modulo(num):
    i = -1
    num = list(str(num))
    while i > -len(num):
        if i % 4 == 1:
            num.insert(i, " ")
        i -= 1
    return "".join(num)

def matches(substr, s):
    m = len(s)
    n = len(substr)
    matches = list()
    if n > m:
        return matches
    if substr == s:
        matches.append((0,n))
        return matches
    for i in range(m-n+1):
        if substr == s[i:n+i]:
            matches.append((i, n+i))
    return matches

def name_meanings():
    n, fam_name = input().split()
    n = int(n)
    # read dictionary
    dictionary = dict()
    for i in range(n):
        word, meanings = input().split()
        dictionary[word] = int(meanings)
    combos = set()
    # for all words in the dictionary
    for word in dictionary:
        # if exact match
        if word == fam_name:
            combos.add(tuple([word]))
        # else if word in family name
        elif word in fam_name:
            # find part or parts of family name that match word
            for match in matches(word, fam_name):
                # for each match:
                    # figure out if rest of family name 
                    # can be matched from dictionary words
                # keep track of substring combo that makes up fam_name
                combo = [word]
                # if beginning of word matches
                if match[0] == 0:
                    for w in dictionary:
                        if fam_name[match[1]:] == w:
                            combo.append(w)
                            # we've matched word
                            combos.add(tuple(combo))
                            break
                # if end of the word matches
                elif match[1] == len(fam_name):
                    for w in dictionary:
                        if fam_name[0:match[0]] == w:
                            combo.insert(0, w)
                            combos.add(tuple(combo))
                            break
                # if middle of word matches
                else:
                    for w in dictionary:
                        if fam_name[0:match[0]] == w:
                            combo.insert(0, w)
                            for w in dictionary:
                                if fam_name[match[1]:] == w:
                                    combo.append(w)
                                    combos.add(tuple(combo))
    print(combos)
    # calculate possible meanings
    possible_meanings = 0
    for combo in combos:
        combo_meanings = list()
        for word in combo:
            combo_meanings.append(dictionary[word])
        possible_meanings += prod(combo_meanings)
    print(modulo(possible_meanings))

if __name__ == "__main__":
    name_meanings()









