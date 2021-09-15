# https://leetcode.com/problems/shortest-bridge/

from pprint import pprint
from typing import *

def neighbors_of(A, coord, predicate):
    '''get neighbors of coord in A satisfying predicate'''
    r, c = coord
    candidates = [
        (r+1, c),
        (r-1, c),
        (r, c+1),
        (r, c-1)
    ]
    return [cand for cand in candidates if predicate(A, coord, cand)]

def get_island(A, coord):
    '''given a matrix A and coordinate coord, find all indices with a path to coord though only character A[coord]'''
    r, c = coord
    ch = A[r][c]

    def neighbor_predicate(A, coord, neighbor_coord):
        r, c = coord
        nr, nc = neighbor_coord
        predicates = [ nr in range(len(A)),
                       nc in range(len(A[0]),
                       A[r][c] == A[nr][nc] ]
        return all(predicates)

    fringe = {coord}
    seen = set()
    distances = {}
    while fringe:
        f = fringe.pop()
        if f in seen:
            continue
        seen.add(f)
        for neighbor in neighbors_of(A, f, neighbor_predicate):
            if neighbor in seen:
                continue
            fringe.add(neighbor)
  

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        island1_coord = identify_island_coordinate(A)
        B = remove_island(island1_coord, A)
        island2_coord = identify_island_coordinate(B)

        distances = initialize_distances(island1_coord, A)
        distances = update_distances(distances, A)
        




testcases = [
    [[0, 1], [1, 0]],
    [[0, 1, 0], [0, 0, 0], [0, 0, 1]],
    [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
]

for t in testcases:
    print(Solution().shortestBridge(t))
