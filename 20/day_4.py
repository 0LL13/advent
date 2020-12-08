# -*- coding: utf-8 -*-
import re
from typing import List


INPUT_1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

INPUT_2 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

INPUT_invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

INPUT_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


with open('./20/input/day_4.txt', 'r') as fin:
    INPUT = fin.read()


def one_pp_one_line(INPUT):
    lines = INPUT.splitlines()
    passports = []
    tmp_line = ''
    for i, line in enumerate(lines):
        # print(i, line)
        if line == '':
            passports.append(tmp_line.strip())
            tmp_line = ''
        else:
            tmp_line = tmp_line + ' ' + line

    passports.append(tmp_line.strip())

    return passports


def check_passport(passport: List[str]) -> bool:
    if len(passport) < 7:
        return False
    elif len(passport) == 7:
        for item in passport:
            if 'cid' in item.split(':'):
                return False
    for item in passport:
        k, v = item.split(':')
        if k == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif k == 'byr':
            if not 1920 <= int(v) <= 2002:
                return False
        elif k == 'iyr':
            if not 2010 <= int(v) <= 2020:
                return False
        elif k == 'eyr':
            if not 2020 <= int(v) <= 2030:
                return False
        elif k == 'hcl':
            if not re.match(r'^#[0-9a-f]{6}$', v):
                return False
        elif k == 'pid':
            if not re.match(r'^\d{9}$', v) or len(v) != 9:
                return False
        elif k == 'hgt':
            if not re.match(r'1[5-8]\dcm$|19[0-3]cm$|59in$|6\din$|7[0-6]in$', v):  # noqa
                return False
    return True


if __name__ == '__main__':
    pp = one_pp_one_line(INPUT)
    print('# of passports:', len(pp))
    count = 0
    for i, passport in enumerate(sorted(pp)):
        valid = True
        fields = passport.split(' ')
        print(i, fields, len(fields), end=' ')
        if len(fields) == 8:
            count += 1
            print('count:', count)
        elif len(fields) == 7:
            for field in fields:
                if 'cid' in field.split(':'):
                    valid = False
            if valid:
                count += 1
            print('count:', count)
        else:
            print()
    print('part 1:', count)

    count = 0
    for i, passport in enumerate(pp):
        if check_passport(passport.split(' ')):
            count += 1

    print()
    print('part 2:', count)
