#!/usr/bin/env python3
# ID: shell
# LANG: PYTHON3
# LINK: https://usaco.org/index.php?page=viewproblem2&cpid=891
import sys

def simulate(guesses, starting) -> int:
    wins = 0
    shell_at = starting
    for guess in guesses:
        a, b, g = guess
        if shell_at in (a, b):
            shell_at = a if shell_at == b else b
        if shell_at == g:
            wins += 1
    return wins
def max_score(guesses) -> int:
    return max([simulate(guesses, starting) for starting in (1, 2, 3)])

if __name__ == "__main__":
    with open("shell.in") as f:
        sys.stdin = f
        N = int(input())
        guesses = []
        for _ in range(N):
            guesses.append(tuple(map(int, input().split())))
        with open("shell.out", "w") as fo:
            print(max_score(guesses), file=fo)