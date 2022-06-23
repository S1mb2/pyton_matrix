def is_cezar(text, key):  # Функция шифрования "Цезарь" eng
    out = []
    temp = []
    for i in range(len(text)):
        for j in text[i]:
            if ord(j) + int(key) > 90 and 91 > ord(j) > 64 or ord(j) + int(
                    key) > 122 and 123 > ord(j) > 96:
                if j.isalpha():
                    temp.append(chr(ord(j) + int(key) - 26))
                else:
                    temp.append(j)
            else:
                if j.isalpha():
                    temp.append(chr(ord(j) + int(key)))
                else:
                    temp.append(j)

        # temp.append(' ')
        out.extend(temp)
        temp.clear()
    return ''.join(out)


def get_shift(st):
    shift = 0
    for c in st:
        if c.isalpha():
            shift += 1
    return shift


s = input().split()
x = list()

for c in range(len(s)):
    shift = get_shift(s[c])
    cesar = [is_cezar(s[c], shift)]
    x += cesar
print(*x)