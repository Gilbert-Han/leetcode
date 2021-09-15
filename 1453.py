# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

from math import sqrt
import numpy as np
from typing import *

def get_result(points, r, v):
    '''check how many points are within r of the vector v'''
    result = 0
    for p in points:
        if np.linalg.norm(p-v) <= r:
            result += 1
    return result

def brute_force(points, r):
    # print(f'brute_force{points}, {r}')
    xs = points[:, 0]
    ys = points[:, 1]
    xrange = range(min(xs), max(xs)+1)
    yrange = range(min(ys), max(ys)+1)
    max_occurances: int = 0
    max_value = None
    for x in xrange:
        for y in yrange:
            v = np.array((x, y))
            result = get_result(points, r, v)
            # print(f'tring {v} -> {result}')
            if result > max_occurances:
                # print(f'>>> taking {v}')
                max_occurances = result
                max_value = v
    return max_occurances


def _numPoints(points: np.ndarray, r: int) -> int:
    return brute_force(points, r)


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        return _numPoints(np.array([np.array(p) for p in points]), r)


if __name__ == '__main__':
    testcases = [
        ([[-2, 0], [2, 0], [0, 2], [0, -2]], 2),
        ([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5),
        ([[-2, 0], [2, 0], [0, 2], [0, -2]], 1),
        ([[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]], 2)
    ]
    expected = [
        4,
        5,
        1,
        4
    ]
    for i, (testcase, expected) in enumerate(zip(testcases, expected)):
        points, r = testcase
        result = Solution().numPoints(points, r)
        if result != expected:
            print(f'failed testcase {i} {testcase}: {result = }, {expected = }')
