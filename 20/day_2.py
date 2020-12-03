# -*- coding: utf-8 -*-
from collections import Counter


INPUT = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


with open('./20/input/day_2.txt', 'r') as fin:
    INPUT = fin.read()


lines = [line for line in INPUT.split('\n') if line]


def rule_check(low: int, hi: int, letter: str, psw: str) -> bool:
    c = Counter(psw)
    if low <= c[letter] <= hi:
        return True
    return False


count = 0
for line in lines:
    rule, sep, psw = line.rpartition(':')
    range_, letter = rule.split(' ')
    low, hi = [int(num) for num in range_.split('-')]
    count += 1 if rule_check(low, hi, letter, psw) else 0

print(count)


def new_rule_check(low: int, hi: int, letter: str, psw: str) -> bool:
    count = 0
    for i, ch in enumerate(psw):
        if ch == letter and i in [hi, low]:
            count += 1

    if count == 1:
        return True
    return False


count = 0
for line in lines:
    rule, sep, psw = line.rpartition(':')
    range_, letter = rule.split(' ')
    low, hi = [int(num) for num in range_.split('-')]
    count += 1 if new_rule_check(low, hi, letter, psw) else 0

print(count)
