import random, sys
import trick
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def generate_password():
    password = []
    [password.append(alph[random.randint(0, len(alph) - 1)]) for i in range(random.randint(10, 20))]
    return ''.join(password)


if len(sys.argv) < 2:
    print('wrong command')
    exit

flag = False # is it change something or it is new password
password_to = input('write tagname (vk, gmail, yandex passport и т.п.)  ... \n')
if sys.argv[1] == 'do':
    password = generate_password()
    data = open('passwords.txt', 'r').read()
    new_data = ''
    for el in data.split('\n'):
        _ = el.split(' : ')
        if len(_) != 2:
            break
        if _[1] == password_to:
            _[0] = password
            flag = True
        new_data += trick.code(_[0]) + ' : ' + _[1] + '\n'
    f = open('passwords.txt', 'w')
    f.write(new_data if flag else new_data + password + ' : ' + password_to)
    f.close()
elif sys.argv[1] == 'get':
    data = open('passwords.txt', 'r').read()
    password = ''
    for el in data.split('\n'):
        _ = el.split(' : ')
        if len(_) != 2:
            break
        if _[1] == password_to:
            flag = True
            password = trick.decode(_[0])
    print('no such password' if not flag else password)
else:
    print('wrong command')
