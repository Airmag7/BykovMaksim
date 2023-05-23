import re


def main(x):
    x = x.replace('\n', ' ')
    matches = re.findall(r"do equ\s?#(-?\d+).*?'(.*?)';", x)
    res = [(match[1], int(match[0])) for match in matches]
    return res


print(main("[do equ #-4041 ==> 'reedti_614'; done;do equ #-7010 ==>'ined'; done; do equ #888 ==> 'getege'; done;]"))
print(main("[ do equ#9683 ==>'uste_317'; done; do equ #-1556 ==>'veenge_205';done;]"))
print(main("[ do equ #-9375==>'enla';done; do equ #-5450==>'inxe_430'; done; do\nequ #-72 ==> 'quar'; done; ]"))