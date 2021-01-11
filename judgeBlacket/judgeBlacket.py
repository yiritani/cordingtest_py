
def validate_format(chars: str)-> bool:
    st = []
    d = {'(': ')', '{': '}', '[': ']'}

    for char in chars:
        if char in d.keys():
            st.append(d[char])
        if char in d.values():
            if not st:
                return False
            if char != st.pop():
                return False

    if st:
        return False

    return True

print(validate_format("{['key1']}"))
