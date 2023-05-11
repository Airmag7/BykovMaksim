import re


def main(data_string):
    pattern = r"do equ #\(\d+) ==>\s+\([\w*])\s*;\s*done;"
    matches = re.findall(pattern, data_string)
    pairs = []
    for match in matches:
        pair = ((match[1])[1:-1], match[0])
        pairs.append(pair)
    return pairs

print(main("[do equ #-4041 ==> 'reedti_614'; done;do equ #-7010 ==>'ined'; done; do equ #888 ==> 'getege'; done;]"))