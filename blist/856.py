#!/usr/bin/env python3
# ID: The Bucket List
# LANG: PYTHON3
# LINK: https://usaco.org/index.php?page=viewproblem2&cpid=856
import bisect
import sys
def max_buckets(N, cows):
    max_b = 0
    cows = sorted(cows)
    print(cows)
    for i in range(1000):
        curr_b = 0
        for s,e,b in cows:
            if s <= i <= e:
                curr_b += b
        max_b = max(max_b, curr_b)
        #print(i, curr_b)
    return max_b
if __name__ == "__main__":
    with open("blist.in") as f:
        sys.stdin = f
        N  = int(input())
        cows = [tuple(map(int, input().split())) for _ in range(N)]
        with open("blist.out", "w") as fo:
            res = max_buckets(N, cows)
            print(res, file=fo)