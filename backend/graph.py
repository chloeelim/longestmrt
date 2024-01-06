import json
import sqlite3
from collections import deque

with open("adj.json") as f:
    data = json.load(f)
    code_to_index = {code: index for index, code in enumerate(data.keys())}
    index_to_code = {index: code for index, code in enumerate(data.keys())}


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
    q = deque()
    q.append((0, start, []))  # shortest, currdist, node
    ans_num = float('-inf')
    ans_path = None
    while q:
        currdist, node, path = q.popleft()

        if node in path:
            continue
        dist[node] = currdist
        if node == end:
            if ans_num < currdist:
                ans_num = currdist
                ans_path = path + [node]

        else:
            for edge in data[node]['edges']:
                q.append((currdist + 1, edge, path + [node]))
    if not len(ans_path):
        print(start, end, "returned none")
    return ans_path


def retrieve_longest_path(start, end):
    with sqlite3.connect("mrt.db") as con:
        cur = con.cursor()
        path = cur.execute(
            "SELECT part FROM path WHERE start = ? AND end = ? ORDER BY index_", (start, end)).fetchall()
        if not path:
            print("wth", path)
            return longest_path(start, end)
        path = [part[0] for part in path]
        return path


codes = list(data.keys())
path_data = {}
n = len(codes)
