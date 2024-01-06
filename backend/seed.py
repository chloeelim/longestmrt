import sqlite3
from graph import codes, longest_path
from alive_progress import alive_bar
import sys

con = sqlite3.connect("mrt.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS path(start, end, index_, part)")
con.commit()
part = int(sys.argv[1])

length = len(codes)
all_pairs = [(codes[i], codes[j]) for i in range(length)
             for j in range(i + 1, length)]
total_iter = len(all_pairs)
NUM_PARTS = 12
one_part = total_iter // NUM_PARTS
start_iter = part * one_part
end_iter = (part + 1) * one_part

with alive_bar(one_part) as bar:
    for k in range(start_iter, end_iter):
        start, end = all_pairs[k]
        path = longest_path(start, end)
        for index, part in enumerate(path):
            cur.execute("INSERT INTO path VALUES (?, ?, ?, ?)",
                        (start, end, index, part))
        # insert the reverse as well
        start, end = end, start
        path = path[::-1]
        for index, part in enumerate(path):
            cur.execute("INSERT INTO path VALUES (?, ?, ?, ?)",
                        (start, end, index, part))
        con.commit()
        bar()
