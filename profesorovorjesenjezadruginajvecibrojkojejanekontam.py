n = int(input("Unesite n: "))

if n < 10000 or n > 99999:
    print("GRESKA!")
else:
    e = n % 10
    n = n // 10
    d = n % 10
    n = n // 10
    c = n % 10
    n = n // 10
    b = n % 10
    n = n // 10
    a = n

    najmanja = a
    if b < najmanja:
        najmanja = b
    if c < najmanja:
        najmanja = c
    if d < najmanja:
        najmanja = d
    if e < najmanja:
        najmanja = e

    maks = a
    maks2 = b

    if b > a:
        maks = b
        maks2 = a

    if c > maks:
        maks2 = maks
        maks = c
    elif c > maks2:
        maks2 = c

    if d > maks:
        maks2 = maks
        maks = d
    elif d > maks2:
        maks2 = d

    if e > maks:
        maks2 = maks
        maks = e
    elif e > maks2:
        maks2 = e

    print(maks, maks2, najmanja, maks2-najmanja)
