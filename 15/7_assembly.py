# -*- coding: utf-8 -*-
"""
case 1: int -> wire
case 2: NOT wire -> wire
case 3: wire l/rshift int -> wire
case 4: wire OR wire -> wire
case 4: wire AND wire -> wire
case 5: 1 AND wire -> wire  # will be 1 or 0 depending if signal or wire is odd
                            # or not
"""
from typing import Dict


INPUT = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


with open('15/input/7_input.txt', 'r') as fin:
    INPUT = fin.read()


def and_gate(sig_left: int, sig_right: int) -> int:
    sig = sig_left & sig_right
    if sig < 0:
        sig = 65536 + sig
    return sig


def or_gate(sig_left: int, sig_right: int) -> int:
    sig = sig_left | sig_right
    if sig < 0:
        sig = 65536 + sig
    return sig


def lshift(sig_left: int, shift: int) -> int:
    sig = sig_left << shift
    if sig < 0:
        sig = 65536 + sig
    return sig


def rshift(sig_left: int, shift: int) -> int:
    sig = sig_left >> shift
    if sig < 0:
        sig = 65536 + sig
    return sig


def bitwise_not(sig_: int) -> int:
    sig = ~sig_
    if sig < 0:
        sig = 65536 + sig

    return sig


def is_known(wires, id_) -> bool:
    for k, v in wires.items():
        if k == id_:
            return True
    return False


def is_int(sig) -> bool:
    try:
        if isinstance(int(sig), int):
            return True
    except ValueError:
        pass
    return False


def assign_sig(wires: dict, sig: str, id_res: str) -> Dict[str, int]:
    wires[id_res] = sig
    return wires


def get_sig(wires: dict, id_: str) -> int:
    for k, v in wires.items():
        if k == id_:
            return v

    raise Exception


def return_sig(wires: dict, id_) -> int:
    if is_int(id_):
        return int(id_)
    else:
        return get_sig(wires, id_)


def get_wires(wires, line):
    fields = line.split(' ')
    id_res = fields[-1]
    if len(fields) == 3:
        wires_ = assign_at_3(wires, fields, id_res)
    elif len(fields) == 4:
        wires_ = assign_at_4(wires, fields, id_res)
    elif len(fields) == 5:
        wires_ = assign_at_5(wires, fields, id_res)
    else:
        wires_ = wires
        # print("Nothing to declare!!!!!!!!!!!!!!!!!!!!!!!!")
        # sys.exit()

    return wires_


def assign_at_3(wires, fields, id_res):
    sig_ = fields[0]
    if is_int(sig_):
        wires_ = assign_sig(wires, int(sig_), id_res)
    elif is_known(wires, sig_):
        sig = get_sig(wires, sig_)
        wires_ = assign_sig(wires, sig, id_res)
    else:
        wires_ = wires

    return wires_


def assign_at_4(wires, fields, id_res):
    sig_ = fields[1]
    if is_known(wires, sig_):
        sig = get_sig(wires, sig_)
        sig = bitwise_not(sig)
        wires_ = assign_sig(wires, sig, id_res)
    else:
        wires_ = wires

    return wires_


def assign_at_5(wires, fields, id_res):
    id_left, command, id_right, sep, id_res = fields
    if command == 'LSHIFT' and is_known(wires, id_left):
        shift = int(id_right)
        sig_left = get_sig(wires, id_left)
        sig = lshift(sig_left, shift)
        wires_ = assign_sig(wires, sig, id_res)
    elif command == 'RSHIFT' and is_known(wires, id_left):
        shift = int(id_right)
        if id_left == 'b':
            sig_left = 956
        else:
            sig_left = get_sig(wires, id_left)
        sig = rshift(sig_left, shift)
        wires_ = assign_sig(wires, sig, id_res)
    elif command == 'AND' and id_left == '1' and is_known(wires, id_right):
        sig_right = get_sig(wires, id_right)
        if sig_right % 2 == 0:
            wires_ = assign_sig(wires, 0, id_res)
        else:
            wires_ = assign_sig(wires, 1, id_res)
    elif command == 'AND' and is_known(wires, id_left) and is_known(wires, id_right):  # noqa
        if id_left == 'b':
            sig_left = 956
        else:
            sig_left = get_sig(wires, id_left)
        sig_right = get_sig(wires, id_right)
        sig = and_gate(sig_left, sig_right)
        wires_ = assign_sig(wires, sig, id_res)
    elif command == 'OR' and is_known(wires, id_left) and is_known(wires, id_right):  # noqa
        if id_left == 'b':
            sig_left = 956
        else:
            sig_left = get_sig(wires, id_left)
        sig_right = get_sig(wires, id_right)
        sig = or_gate(sig_left, sig_right)
        wires_ = assign_sig(wires, sig, id_res)
    else:
        wires_ = wires

    return wires_


if __name__ == '__main__':
    wires: Dict[str, int] = {}
    INPUT_ = [inp for inp in INPUT.split('\n') if inp]
    len_INPUT = len(INPUT_)
    i = 0
    counter = 0
    while INPUT_:
        if len_INPUT == 0:
            break
        elif i >= len_INPUT:
            i = 0
        line = INPUT_[i]
        wires_ = get_wires(wires, line)
        if len(wires.keys()) == len_INPUT:
            break
        i += 1

    for wire, sig in wires.items():
        print(wire, sig)
