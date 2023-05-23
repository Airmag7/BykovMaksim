import re


def main(x):
    x = x.replace('\n', ' ')
    matches = re.findall(r"\[\s?variable\s?#\s?(-?\d+)\s*\s?\|>"
                         r"\s?\s*\s?`([^\s;]+)\.", x)
    result = [(m[1], int(m[0])) for m in matches]
    return result


print(main("<block> [variable#-9439 |>`rabi_731.]; [ variable #2196|>`ladi.];[variable #9601 |>`useron. ]; </block>"))
print(main("<block> [ variable #-8835 |> `anon_90.];[variable #-1215 |> `xeedbe.];</block>"))