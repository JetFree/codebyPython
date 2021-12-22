access = {'admin': 'megapass', 'mazhor': 'goldkey777',
'chuvak': 'all_good', 'lelik': 'bablo_forever',
'invisible_man': 'a1dfvb5415vD', 'LOL': 12345}

print(str(access).replace('{', '').replace('}', '').replace('\'', '')
      .replace(", ", '\n'))
