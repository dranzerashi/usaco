#!/usr/bin/env python3
# ID: Amplify Signal
# LANG: PYTHON3
# LINK: https://usaco.org/index.php?page=viewproblem2&cpid=665
import bisect
import sys
def amplify_signal(signal, N, K):
    res = []
    for line in signal:
        amplified_line = ''.join([ch*K for ch in line])
        res.extend([amplified_line]*K)
    return res
if __name__ == "__main__":
    with open("cowsignal.in") as f:
        sys.stdin = f
        M, N, K  = map(int, input().split())
        signal = [input() for _ in range(M)]
        with open("cowsignal.out", "w") as fo:
            res = amplify_signal(signal, N, K)
            for line in res:
                print(line, file=fo)