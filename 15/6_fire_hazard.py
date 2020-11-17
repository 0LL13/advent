# -*- coding: utf-8 -*-
from collections import namedtuple


Point = namedtuple('Point', 'x, y, state')


def initialize_grid():
    grid = []
    for i in range(1000):
        for j in range(1000):
            point = Point(x=i, y=j, state=0)
            grid.append(point)

    return grid


def turn_on(point) -> Point:
    x = point.x
    y = point.y
    # state = "on"
    state = point.state + 1

    return Point(x, y, state)


def turn_off(point) -> Point:
    x = point.x
    y = point.y
    # state = "off"
    state = point.state - 1
    if state < 0:
        state = 0

    return Point(x, y, state)


def toggle(point) -> Point:
    x = point.x
    y = point.y
#     if state == "on":
#         state = "off"
#     else:
#         state = "on"
    state = point.state + 2

    return Point(x, y, state)


def turn_area_on(point_1, point_2, grid):
    grid_ = grid[:]
    for i, point in enumerate(grid_):
        if point.x >= point_1.x and point.x <= point_2.x:
            if point.y >= point_1.y and point.y <= point_2.y:
                grid[i] = turn_on(point)

    return grid


def turn_area_off(point_1, point_2, grid):
    grid_ = grid[:]
    for i, point in enumerate(grid_):
        if point.x >= point_1.x and point.x <= point_2.x:
            if point.y >= point_1.y and point.y <= point_2.y:
                grid[i] = turn_off(point)

    return grid


def toggle_area(point_1, point_2, grid):
    grid_ = grid[:]
    for i, point in enumerate(grid_):
        if point.x >= point_1.x and point.x <= point_2.x:
            if point.y >= point_1.y and point.y <= point_2.y:
                grid[i] = toggle(point)

    return grid


def get_instructions(line):
    instructions = line.split('through')
    x2, y2 = instructions[-1].strip().split(',')
    point_2 = Point(int(x2), int(y2), 'off')
    rest = [el.strip() for el in instructions[0].split(' ') if el.strip()]
    x1, y1 = rest[-1].strip().split(',')
    point_1 = Point(int(x1), int(y1), 'off')
    if rest[0] == 'toggle':
        switch = 'toggle'
    elif rest[1] == 'on':
        switch = 'on'
    elif rest[1] == 'off':
        switch = 'off'

    return switch, point_1, point_2


if __name__ == '__main__':
    with open('6_input.txt', 'r') as fin:
        lines = fin.read().split('\n')

    lines = [line.strip() for line in lines if line.strip()]
    grid = initialize_grid()

    for i, line in enumerate(lines):
        switch, point_1, point_2 = get_instructions(line)
        if switch == 'on':
            turn_area_on(point_1, point_2, grid)
        elif switch == 'off':
            turn_area_off(point_1, point_2, grid)
        else:
            toggle_area(point_1, point_2, grid)

    counter = 0
    for point in grid:
        counter += point.state

    print(counter)
