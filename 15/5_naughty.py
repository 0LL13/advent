# -*- coding: utf-8 -*-
def first_set_of_rules():
    data = get_data()
    vowel_strings = []
    for line in data.split('\n'):
        if has_3_vowels(line):
            vowel_strings.append(line.strip())

    double_strings = []
    for line in vowel_strings:
        if has_double(line):
            double_strings.append(line)

    nice_strings = []
    for line in double_strings:
        if has_no_naughty(line):
            nice_strings.append(line)

    for i, line in enumerate(nice_strings):
        print(i, line)

    return len(nice_strings)


def has_3_vowels(line) -> bool:
    counter = 0
    for ch in line:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
            if counter == 3:
                return True
    return False


def has_double(line) -> bool:
    for i, ch in enumerate(line):
        ll = len(line)
        if i < ll:
            if ch == line[i+1]:
                return True
    return False


def has_no_naughty(line) -> bool:
    for i, ch in enumerate(line):
        if i >= 1:
            if line[i-1] + ch in ['ab', 'cd', 'pq', 'xy']:
                return False
    return True


def get_data():
    with open('./input/5_input.txt', 'r') as fin:
        data = fin.read()
    return data


def second_set_of_rules():
    data = 'qjhvhtzxzqqjkmpb\nxxyxx\nuurcxstgmygtbstg\nieodomkazucvgmuy'  # noqa
    data = get_data()
    double_pairs = list()
    for line in data.split('\n'):
        if has_double_pair(line):
            double_pairs.append(line.strip())

    sandwiches = []
    for line in double_pairs:
        if has_sandwich(line):
            sandwiches.append(line)

    for i, line in enumerate(sandwiches):
        print(i, line)

    print(len(sandwiches))


def has_double_pair(line) -> bool:
    pairs = []
    for i, ch in enumerate(line):
        ll = len(line)
        if i <= ll and i > 0:
            pair = line[i-1] + ch
            pairs.append(pair)

    check = pairs[:]
    for i, pair in enumerate(pairs):
        if i < len(pairs):
            for j, el in enumerate(check):
                if pair == el and j > i+1:
                    # print(i, line, pairs, pair)
                    return True
    return False


def has_sandwich(line) -> bool:
    for i, ch in enumerate(line):
        if i >= 2:
            if line[i-2] == ch and ch != line[i-1]:
                return True
    return False


if __name__ == '__main__':
    second_set_of_rules()
