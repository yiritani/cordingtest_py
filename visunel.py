import string


def generate_key(secret) -> str:
    key = secret
    remain_len = len(public) - len(secret)
    for i in range(remain_len):
        key += key[i]
    return key


def visunel(public, key):
    answer_index = string.ascii_uppercase
    result = ''
    for i in range(len(public)):
        if public[i] not in answer_index:
            result += public[i]
            continue
        index = ((ord(public[i]) + ord(key[i])) % 26)
        result += answer_index[index]
    return result


def visunel_hack(encrypt, key):
    answer_index = string.ascii_uppercase
    result = ''
    for i, k in enumerate(encrypt):
        if encrypt[i] not in answer_index:
            result += encrypt[i]
            continue
        index = (ord(encrypt[i]) - ord(key[i]) + 26) % 26
        result += answer_index[index]

    print(result)


public = 'ATTACK SILION VALLEY'
secret = 'HELLO'
key = generate_key(secret)
e = visunel(public, key)
print(e)
visunel_hack(e, key)
