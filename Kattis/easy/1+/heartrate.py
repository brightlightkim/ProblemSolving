times = int(input())

for _ in range(times):
    b, p = input().split()

    bpm = 60 * float(b) / float(p)
    abpm = 60 / float(p)
    print("%0.4f" % (bpm - abpm), "%0.4f" % bpm, "%0.4f" % (bpm + abpm))