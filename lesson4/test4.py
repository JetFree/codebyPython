number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
result_list = [number[-1]*2, number[0] + symbol[4], number[-3] + symbol[2],
          number[1] + number[5], symbol[0] + number[0], symbol[2] + number[-3]]
result_str = ":".join(result_list)
print(result_str)
