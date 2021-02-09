import string
from typing import Generator, Tuple

def ceaser(sentence: str, shift: int):
    result = ''
    len_alphabet = ord('Z') - ord('A') + 1

    for i in sentence:
        # if i.isupper():
        #     alphabet = string.ascii_uppercase
        # elif i.islower():
        #     alphabet = string.ascii_lowercase
        # else:
        #     result += i
        #     continue
        #
        # index = (alphabet.index(i) + shift) % len(alphabet)
        # result += alphabet[index]
        if i.isupper():
            result += chr((ord(i) + shift - ord('A')) % len_alphabet + ord('A'))
        elif i.islower():
            result += chr((ord(i) + shift - ord('a')) % len_alphabet + ord('a'))
        else:
            result += i
            continue

    return result


def decrypt_ceaser(encrypt) -> Generator[Tuple[int,str], None, None]:
    for c in range(1, len(string.ascii_uppercase)):
        result = ''
        for i in encrypt:
            if i.isupper():
                result += chr((ord(i) + c - ord('A')) % 26 + ord('A'))
            elif i.islower():
                result += chr((ord(i) + c - ord('a')) % 26 + ord('a'))
            else:
                result += i
        yield c, result


e = ceaser('ZSILLICON VALLY engineer', 3)
for i in decrypt_ceaser(e):
    print(i)


# print(ceaser('A', 3))
# ceaser('A')