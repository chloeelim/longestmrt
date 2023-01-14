import time
import json
from heapq import heappop, heappush

with open("adj.json") as f:
    data = json.load(f)
    code_to_index = {code: index for index, code in enumerate(data.keys())}


# test: DT2, TE4


def floyd_warshall():
    # precompute first
    count = len(data)
    dist = [[float('inf')] * count for _ in range(count)]
    for code, station in data.items():
        dist[code_to_index[code]][code_to_index[code]] = 0
        for edge in station['edges']:
            dist[code_to_index[code]][code_to_index[edge]] = 1
            dist[code_to_index[edge]][code_to_index[code]] = 1
    for k in range(count):
        for i in range(count):
            for j in range(count):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


shortest = floyd_warshall()


def longest_path(start, end):
    """return longest path from start -> end"""
    dist = {}
    pq = [(0, 0, start, [])]  # shortest, currdist, node
    ans_num = float('-inf')
    ans_path = None
    while pq:
        s, currdist, node, path = heappop(pq)
        if node in dist and dist[node] > currdist or node in path:
            continue
        dist[node] = currdist
        if node == end:
            if ans_num < currdist:
                ans_num = currdist
                ans_path = path + [node]

        else:
            for edge in data[node]['edges']:
                heappush(
                    pq, (shortest[code_to_index[node]][code_to_index[edge]], currdist + 1, edge, path + [node]))

    return ans_path
