def fox_noises():
    t = int(input())
    for i in range(t):
        recording = input().split()
        noise = input()
        while noise != "what does the fox say?":
            noise = noise.split()[-1]
            while noise in recording:
                recording.remove(noise)
            noise = input()
        print(" ".join(recording))

if __name__ == "__main__":
    fox_noises()