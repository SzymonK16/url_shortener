import string

def encode_base62(num: int) -> str:
    characters = string.digits + string.ascii_lowercase + string.ascii_uppercase
    if num == 0:
        return characters[0]

    res = []
    while num:
        res.append(characters[num % 62])
        num //= 62
    return "".join(reversed(res))