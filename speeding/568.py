#!/usr/bin/env python3
# ID: speeding
# LANG: PYTHON3
# LINK: https://usaco.org/index.php?page=viewproblem2&cpid=568
import bisect
import sys
def worst_violation(segments, speeds) -> int:
    max_violation = 0
    road_speed_limits = []
    curr_length = 0
    for segment in segments:
        length, speed_limit = segment
        road_speed_limits.append((curr_length+length, speed_limit))
        curr_length += length
    curr_length = 0
    for segment, speed in speeds:
        new_length = curr_length + segment
        start_index = bisect.bisect_right(road_speed_limits, (curr_length+1, 0))
        end_index = bisect.bisect_right(road_speed_limits, (new_length, 0))
        for i in range(start_index, end_index+1):
            max_violation = max(max_violation, speed - road_speed_limits[i][1])
        #print(start_index, end_index, curr_length+1, new_length, road_speed_limits, max_violation)
        curr_length = new_length
    return max_violation
if __name__ == "__main__":
    with open("speeding.in") as f:
        sys.stdin = f
        N, M = map(int, input().split())
        segments = [tuple(map(int, input().split())) for _ in range(N)]
        speeds = [tuple(map(int, input().split())) for _ in range(M)]
        with open("speeding.out", "w") as fo:
            print(worst_violation(segments, speeds), file=fo)