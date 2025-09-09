#!/usr/bin/env python3
# ID: The Bovine Shuffle
# LANG: PYTHON3
# LINK: https://usaco.org/index.php?page=viewproblem2&cpid=760
import bisect
import sys
def deshuffle(shuffle, cows, N):
    res = list(cows)
    for i in range(3):
        curr = list(res)
        for j,s in enumerate(shuffle):
            curr[j] =  res[s-1]
        res = curr
    return res
if __name__ == "__main__":
    with open("shuffle.in") as f:
        sys.stdin = f
        N  = int(input())
        shuffle = list(map(int, input().split()))
        cows = input().split()
        with open("shuffle.out", "w") as fo:
            res = deshuffle(shuffle, cows, N)
            for line in res:
                print(line, file=fo)