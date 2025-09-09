#!/usr/bin/env python3
# ID: mixmilk
# LANG: PYTHON3
# LINK: https://usaco.org/index.php?page=viewproblem2&cpid=855
import bisect
import sys
def find_final_state(c1, m1, c2, m2, c3, m3):
    r1, r2, r3 = m1, m2, m3
    for i in range(100):
        if i%3 == 0:
            pour = min(r1, c2 - r2)
            r1 -= pour
            r2 += pour
        elif i%3 == 1:
            pour = min(r2, c3 - r3)
            r2 -= pour
            r3 += pour
        elif i%3 == 2:
            pour = min(r3, c1 - r1)
            r3 -= pour
            r1 += pour
        #print(r1, r2, r3)
    return (r1, r2, r3)
if __name__ == "__main__":
    with open("mixmilk.in") as f:
        sys.stdin = f
        c1, m1  = map(int, input().split())
        c2, m2 = map(int, input().split())
        c3, m3 = map(int, input().split())
        with open("mixmilk.out", "w") as fo:
            r1, r2, r3 = find_final_state(c1, m1, c2, m2, c3, m3)
            print(r1, file=fo)
            print(r2, file=fo)
            print(r3, file=fo)