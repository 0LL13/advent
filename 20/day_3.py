# -*- coding: utf-8 -*-
from typing import List


INPUT = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


with open('./20/input/day_3.txt', 'r') as fin:
    INPUT = fin.read().strip()


lines = INPUT.split('\n')
line_length = len(lines[0])
print(len(lines))


def count_trees(line_length: int, right: int, down: int, lines: List[str]) -> int:  # noqa
    tot_lines = len(lines)
    trees = 0
    j = 0
    i = 0
    for _ in range(tot_lines):
        # print("  0123456789")
        # print(i, line, end=" ---> ")
        if i+down <= tot_lines - down:
            i += down
            next_line = lines[i]
            j = (j + right) % line_length
            ch = next_line[j]
            # print("i, j, ch:", i, j, ch)
            if ch == '#':
                trees += 1

    return trees


directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = count_trees(line_length, 3, 1, lines)
print('trees first part', trees)

prod = 1
for right, down in directions:
    trees = count_trees(line_length, right, down, lines)
    # print(trees)
    prod *= trees

print(prod)
