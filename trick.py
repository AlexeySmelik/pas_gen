alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def code(string):
    new_string = ''
    for shift in range(len(string)):
        new_string += alph[(alph.index(string[shift]) + shift) % len(alph)]
    return new_string

def decode(string):
    new_string = ''
    for shift in range(len(string)):
        new_string += alph[(len(alph) + alph.index(string[shift]) - shift) % len(alph)]
    return new_string