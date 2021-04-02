import time

def padZeros(numString, numZeros, front):
    for i in range(numZeros):
        if front:
            numString = '0' + numString
        else:
            numString = numString + '0'
    return numString

def karatsuba(x, y):
    x = str(x)
    y = str(y)

    #Base case here is when BOTH x and y are one charater strings
    if len(x) == 1 and len(y) == 1:
            return int(x) * int(y)

    #Checking to make sure that there are an equal amount of digits in each string, if not we pad them with zeros
    if len(x) < len(y):
        #print("we in here??")
        x = padZeros(x, len(y) - len(x), True)
    elif len(y) < len(x):
        #print(y)
        y = padZeros(y, len(x) - len(y), True)
        #print(y)

    #This allows adds 1 zero to the front when numbers are odd length so that they may be evenly split
    # ie: 231 becomes 0231 so that it can be split into 02 and 31 etc.
    if len(y) == len(x) and len(x)%2 != 0:
        x = padZeros(x, 1, True)
        y = padZeros(y, 1, True)

    #
    n = len(x)
    nHalf = int(n/2)

    #keeping track of precision for later
    p2Pad = n - nHalf
    p1Pad = p2Pad * 2

    #splitting x and y into a b c and d. 2211 3214 becomes a = 22, b = 11, c = 32, d = 14
    #this is just done with simple loopty loops
    a = ""
    for i in range(0, nHalf):
        a = a + x[i]
    a = int(a)

    b = ""
    for i in range(nHalf, len(x)):
        b = b + x[i]
    b = int(b)

    c = ""
    for i in range(0, nHalf):
        c = c + y[i]
    c = int(c)

    d = ""
    for i in range(nHalf, len(y)):
        d = d + y[i]
    d = int(d)

    #calculating each of our components
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    temp = karatsuba(a+b, c+d)

    #essentially doing bit shifts here to ensure proper precision
    p1 = int(padZeros(str(ac), p1Pad, False))
    p2 = int(padZeros(str(temp - ac - bd), p2Pad, False))
    return p1 + p2 + bd


#print(karatsuba(2101, 1130))
start = time.time()
print(karatsuba(123123123412367121234, 9233312357342342311111111112367882346742456442342341233))
end = time.time()
print("Calculated in: ", end - start)