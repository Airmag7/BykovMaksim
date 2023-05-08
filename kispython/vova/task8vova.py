import re


def main(data_string):
    pattern = r"`(\w+)\s?=>\s?@(.*?)\.\s*</data>"
    matches = re.findall(pattern, data_string)
    pairs = []
    for match in matches:
        pair = ((match[1])[1:-1], match[0])
        pairs.append(pair)
    return pairs

print(main('<<<data> store `raar => @"oraton". </data>;<data> store `raarqu_456\n=> @"mabi_646".</data>; <data>store `ceince_994 => @"maarxe_558".\n</data>; <data> store `atonso_935=>@"qudiri". </data>; >>'))