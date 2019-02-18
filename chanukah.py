thousands = {
                0 : 0,
                1000 : 501500,
                2000 : 2003000,
                3000 : 4504500,
                4000 : 8006000,
                5000 : 12507500,
                6000 : 18009000,
                7000 : 24510500,
                8000 : 32012000,
                9000 : 40513500,
                10000 : 50015000            
            }

hundreds = {
                0 : 0,
                100 : 5150,
                200 : 20300,
                300 : 45450,
                400 : 80600,
                500 : 125750,
                600 : 180900,
                700 : 246050,
                800 : 321200,
                900 : 406350                
            }

tens = {
            0 : 0,
            10 : 65,
            20 : 230,
            30 : 495,
            40 : 860,
            50 : 1325,
            60 : 1890,
            70 : 2555,
            80 : 3320,
            90 : 4185
        }

ones = {
        0 : 0,
        1 : 2,
        2 : 5,
        3 : 9,
        4 : 14,
        5 : 20,
        6 : 27,
        7 : 35,
        8 : 44,
        9 : 54
        }

def nearest_thou(n):
    if n < 1000:
        return 0
    if n == 10000:
        return 10000
    return int(str(n)[-4] + "000")

def nearest_hundo(n):
    if n < 100:
        return 0
    return int(str(n)[-3] + "00")

def nearest_ten(n):
    if n < 10:
        return 0
    return int(str(n)[-2] + "0")

def get_one(n):
    return int(str(n)[-1])

def chanukah():
    for i in range(int(input())):
        line = input().split()
        n = int(line[1])
        thou = nearest_thou(n)
        hundo = nearest_hundo(n)
        ten = nearest_ten(n)
        one = get_one(n)
        print(line[0], int(thousands[thou] + hundreds[hundo] + tens[ten] + ones[one]))

if __name__ == "__main__":
    chanukah()