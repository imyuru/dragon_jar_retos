check = 1

if not check:
    print("flag{n1ce_0ne_but_no}")
else:
    v2 = [
        99, 105, 94, 100, 120, 111, 45, 45, 113, 104, 46, 113, 92, 102, 112,
        92, 107, 45, 113, 92, 46, 48, 48, 52, 122
    ]

    for i in range(len(v2)):
        a1 = 3
        print(chr(v2[i] + a1), end='')

    print()
