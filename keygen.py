import sys

seed = sys.argv[1]
key = sys.argv[2]
key = int(key)
result = [0 for i in range(len(seed))]

for i in range(len(seed)):
    # if not seed[i].isalpha() or seed[i].isdigit():
    #     break

    if 97 <= ord(seed[i]) <= 122:
        start = 97
        end = 122
    if 65 <= ord(seed[i]) <= 90:
        start = 65
        end = 90
    if 48 <= ord(seed[i]) <= 57:
        start = 48
        end = 57

    r = end - start + 1

    result[i] = ord(seed[i]) - (key % r)

    wrap = start - result[i]

    if wrap > 0:
        result[i] = end + 1 - wrap

    result[i] = chr(result[i])


for i in range(len(result)):
    if i == 4 or i == 8 or i == 12 or i == 16:
        print('-', end="")

    print(result[i], end="")




