"""Given a string, replace every letter with its position in alphabet and ASCII CODE"""

"""dictionary function"""


def alphabet(el):
    choices = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    return choices.get(el, 0)


if __name__ == '__main__':
    str = "The sunset sets at twelve o' clock."

    print(str)

    r = list(str)

    a = list(str.lower())

    for i in range(len(r)):
        alpha = r[i]
        r[i] = ord(alpha)

    print("ASCII for string is:\n", r)

    for j in range(len(a)):
        el = alphabet(a[j])
        a[j] = el

    while 0 in a:
        a.remove(0)

    print("Alphabet position for string is:\n", a)



