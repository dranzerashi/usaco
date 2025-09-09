#!/usr/bin/env python3
# ID: lostcow
# LANG: PYTHON3
# LINK: https://usaco.org/index.php?page=viewproblem2&cpid=735
import bisect
import sys
def distance(x, y) -> int:
    distance = 0
    at = x
    step = 1
    direction = 1
    no_of_direction_changes = 0
    while at!=y:
        distance += 1
        at += direction
        step -= 1
        if step == 0:
            no_of_direction_changes += 1
            step = 2**no_of_direction_changes + abs(at - x)
            direction *= -1
    return distance
if __name__ == "__main__":
    with open("lostcow.in") as f:
        sys.stdin = f
        x, y = map(int, input().split())
        with open("lostcow.out", "w") as fo:
            print(distance(x,y), file=fo)