tool = 'Super-Puper MainTool /v2*'
tool = tool[:5] + tool[16:-1]
tool = tool.replace("/", "").replace("*", "").replace("2", "1")
width = 20
print("*" * width)
print(tool.center(width, "-"))
print("*" * width)
