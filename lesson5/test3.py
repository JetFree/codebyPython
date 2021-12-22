alles = ('__init__', '127.0.0.1', 'admin', 'SupermAn', 'ClOwN', 'http://site.com',
'humorist', 'https://example.com', '192.168.12.101', 12345, 'https://yandex.ru')

data_dict = {"Login": (alles[2:7:4]), "Password": (alles[3:5]), "IP": alles[1::7],
             "Host": alles[5:8:2]}

print('\033[1m' + list(data_dict.keys())[0] + '\033[0m')
print('\n'.join(data_dict.get("Login")))

print('\033[1m' + list(data_dict.keys())[1] + '\033[0m')
print('\n'.join(data_dict.get("Password")))

print('\033[1m' + list(data_dict.keys())[2] + '\033[0m')
print('\n'.join(data_dict.get("IP")))

print('\033[1m' + list(data_dict.keys())[3] + '\033[0m')
print('\n'.join(data_dict.get("Host")))
