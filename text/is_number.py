def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass

    return False


print(is_number('tun'))
print(is_number('1.5'))
print(is_number('-1.2'))
print(is_number('le3'))

# 阿拉伯语 5
print(is_number('٥'))