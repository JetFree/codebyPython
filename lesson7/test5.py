number = '32106545201261501504165246950415879105101705261210119015261201652094' \
         '1501206206'

print(sum([int(number[i:i + 2]) for i in range(0, len(number), 2)]))