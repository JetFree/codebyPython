address = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
part_1 = "".join([address[0], address[6], address[1]])
final_str = ".".join([part_1, address[-1], address[-1], address[0]])
print(final_str)
