from pwn import *
import string
import time
import statistics

charset = string.ascii_letters + string.digits + "_{}"

flag = "picoCTF{"

while not flag.endswith("}"):
    timings = []

    for ch in charset:
        candidate = flag + ch

        samples = []

        for _ in range(7):
            start = time.perf_counter_ns()
            p = process(["./a", candidate])
            p.recvall(timeout=0.2)
            elapsed = time.perf_counter_ns() - start
            p.close()
            samples.append(elapsed)

        score = statistics.median(samples)

        timings.append((score, ch))

        print(candidate, score)

    timings.sort(reverse=True)

    best = timings[0][1]

    flag += best

    print("FLAG:", flag)
