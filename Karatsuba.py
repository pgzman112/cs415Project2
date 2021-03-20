def padZeros(numString, numZeros, front):
    for i in range(numZeros):
        if front:
            numString = '0' + numString
        else:
            numString = numString + '0'
    return numString

def karatsuba(x, y):
    #print("what time? ", x, y)
    x = str(x)
    y = str(y)
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    #Checking to make sure that there are an equal amount of digits in each string, if not we pad them with zeros
    if len(x) < len(y):
        x = padZeros(x, len(y) - len(x), True)
    elif len(y) < len(x):
        y = padZeros(y, len(x)- len(x), True)

    n = len(x)
    nHalf = int(n/2)

    #This is needed for odd cases
    if (n%2) != 0:
        nHalf += 1
    #Need these values to maintain proper digit precision later
    p2Pad = n - nHalf
    p1Pad = p2Pad * 2

    print("x and y: ", x, " ", y)
    print("n and nHalf: ", n, " ", nHalf, " p2Pad and p1Pad: ", p1Pad, " ", p2Pad)

    a = ""
    for i in range(0, nHalf):
        a = a + x[i]
    a = int(a)

    b = ""
    for i in range(nHalf, len(x)):
        b = b + x[i]
        print("PUSHING: ", x[i])
    b = int(b)

    c = ""
    for i in range(0, nHalf):
        c = c + y[i]
    c = int(c)

    d = ""
    for i in range(nHalf, len(y)):
        d = d + y[i]
    d = int(d)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    temp = karatsuba(a+b, c+d)

    print("ac before: ",ac)
    p1 = int(padZeros(str(ac), p1Pad, False))
    print("ac after pad: ", p1)
    p2 = int(padZeros(str(temp - ac - bd), p2Pad, False))
    return p1 + p2 + bd


#print(karatsuba(2101, 1130))
print(karatsuba(99, 999))
