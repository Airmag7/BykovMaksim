import re


def main(x):
    x = x.replace('\n', ' ')
    matches = re.findall(r'do val (\w+) ?<- (-?\d+);', x)
    result = [(m[0], int(m[1])) for m in matches]
    return result


print(main("((do val inbeed_136<- 9947; end; do val enmage_947<- 9641;end; do val onatve_308 <- 9793; end;do val veat_509<- -8088; end; ))"))
print(main("(( do val soqu<- -9621;end; do val celaso <- 1974; end; do val esmave_423 <- -3228;end;do val ratete <- -8761; end; ))"))