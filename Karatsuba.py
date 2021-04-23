#Preston Zimmerman
#Diana Acre
#4/6/2021

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#Needed a function that would add zeros to the front of the back of strings
#Pretty straight forward
def padZeros(numString, numZeros, front):
    for i in range(numZeros):
        if front:
            numString = '0' + numString
        else:
            numString = numString + '0'
    return numString

#Needed a function to do that sweet sweet exponentiation
#This is from my project 1
def decByCons(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        #THIS IS A STRING (WHICH IS AN ARRAY OF CHARS)
        temp = str(decByCons(a, n/2))
        return karatsuba(str(temp), str(temp))
    else:
        # THIS IS A STRING (WHICH IS AN ARRAY OF CHARS)
        temp = str(decByCons(a, (n-1)/2))
        # KARATSUBA returns an array of chars (string)
        temp1 = karatsuba(a, str(temp))
        return karatsuba(str(temp1), str(temp))

def decByConsWithGradeSchool(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        #THIS IS A STRING (WHICH IS AN ARRAY OF CHARS)
        temp = str(decByConsWithGradeSchool(a, n/2))
        return gradeSchool(str(temp), str(temp))
    else:
        # THIS IS A STRING (WHICH IS AN ARRAY OF CHARS)
        temp = str(decByConsWithGradeSchool(a, (n-1)/2))
        # KARATSUBA returns an array of chars (string)
        temp1 = gradeSchool(a, str(temp))
        return gradeSchool(str(temp1), str(temp))

#This adds 2 strings together using no ints higher than 19. in the case of 9 + 9 + carryOfOne = 19. thats the
#highest int that will be calculated ever
def addStrings(string1, string2):
    #ok lets go
    #make sure we're wroking with strings, since python is funky and who knows what its doing behind the scenes im going to
    #force these to be strings just in case.
    string1 = str(string1)
    string2 = str(string2)
    #We need to make indicys of different length strings. So in the case we want to add 103 and 23561 we change 103 to be 00103
    if len(string1) < len(string2):
        string1 = padZeros(string1, len(string2) - len(string1), True)
    elif len(string2) < len(string1):
        string2 = padZeros(string2, len(string1) - len(string2), True)

    #Here is our overall sum tally
    sum = ""
    carry = 0
    for i in range(len(string1)-1, -1, -1):
        #Adding the current indecies and the carry
        temp1 = int(string1[i])
        temp2 = int(string2[i])
        temp3 = temp1 + temp2 + carry
        #if answer is greater than 9 we set the new carry if not we zero out the carry
        if temp3 > 9:
            carry = 1
        else:
            carry = 0

        #in the case that we had a carry this will lop it off. so 11 -> 1, 15 -> 5, 8 -> 8.
        temp3 = temp3%10
        #concatinate our current index onto our sum
        sum = str(temp3) + sum
    #In the end if theres still a carry we must make sure we don't forget it!
    if carry == 1:
        sum = '1' + sum
    return sum

# A little funky funk to subtract some stringy strings. getting pretty lit up in here.
def subtractStrings(string1, string2):
    #first we determin which is bigger or smaller. for this example I determined I didnt ever want to end up with a negative
    #therefor I just figure out which is bigger, first we can check string length. next if they are the same length we can
    #loop through and determine indicy by indicy which is bigger.
    bigger = ""
    smaller = ""
    ans = ""
    string1 = str(string1)
    string2 = str(string2)
    if len(string1) < len(string2):
        bigger = string2
        smaller = string1
        smaller = padZeros(smaller, len(string2) - len(string1), True)
    elif len(string2) < len(string1):
        bigger = string1
        smaller = string2
        smaller = padZeros(smaller, len(string1) - len(string2), True)
    else:
        for i in range(0, len(string1)):
            if int(string1[i]) > int(string2[i]):
                bigger = string1
                smaller = string2
                break
            elif int(string2[i]) > int(string1[i]):
                bigger = string2
                smaller = string1
                break
        if bigger == "" or smaller == "":
            return str(0)

    #Converting the strings to a list because python is a horrible language
    #and strings are immutable. gross. I am used to c++ where that is not the case.
    arrBig = list(bigger)
    arrSmall = list(smaller)

    #Loop through our lists, starting from the last indicy.
    for i in range(len(bigger)-1, -1, -1):
        #test for the case that we need to do some borrowing!
        if int(arrBig[i]) < int(arrSmall[i]):
            #Need to borrow!
            j = i-1
            #Using a while loop to loop through the bigger list until we find ANYTHING to borrow from
            #that is not a 0
            while arrBig[j] == 0:
                j-=1
            #Once we've found a non zero char to borrow from we subtract that indicy by one (this is why we had to
            # to use a list instead of string because python doesnt allow indicys of a string to be changed even though you can access them)
            arrBig[j] = int(arrBig[j])-1
            j+=1
            #Loop back to our ith index changing any zeros to 9s, taking care of a number like 10000003 - 01000005 where to do 3-5 you need to borrow from that very first 1.
            # it also moves j back towards i
            while j != i:
                arrBig[j] = '9'
                j+=1
            arrBig[i] = int(arrBig[j]) + 10
            temp = int(arrBig[i]) - int(arrSmall[i])
            #Pop the answer onto the front of our string answer
            ans = str(temp) + ans
        else:
            #we don't need to borrow so ez pz.
            temp = int(arrBig[i]) - int(arrSmall[i])
            ans =  str(temp) + ans
    #Removing any leading zeros from the answer.
    arrAns = list(ans)
    realAns = ""
    leadingZeroFlag = False
    for i in range(0, len(arrAns)):
        if(leadingZeroFlag == False):
            if arrAns[i] != '0':
                leadingZeroFlag = True
                realAns = realAns + str(arrAns[i])
        else:
            realAns = realAns + str(arrAns[i])
    #print ("REAL ANS: ",realAns)
    return realAns

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
    p1Pad = n
    p2Pad = nHalf

    #splitting x and y into a b c and d. 2211 3214 becomes a = 22, b = 11, c = 32, d = 14
    #this is just done with simple loopty loops
    #Origionally I was then casting these substrings to ints to make adding them easier later on But I figured you
    #Wouldnt be down with that so I wrote functions to add and subtract strings indicy by indicy it was exciting
    a = ""
    for i in range(0, nHalf):
        a = a + x[i]
    #a = int(a)

    b = ""
    for i in range(nHalf, len(x)):
        b = b + x[i]
    #b = int(b)

    c = ""
    for i in range(0, nHalf):
        c = c + y[i]
    #c = int(c)

    d = ""
    for i in range(nHalf, len(y)):
        d = d + y[i]
    #d = int(d)

    #calculating each of the components
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    aPlusB = addStrings(a, b)
    cPlusD = addStrings(c, d)
    temp = karatsuba(aPlusB, cPlusD)

    #essentially doing bit shifts here to ensure proper precision
    #this is the 10^n * ac but without using multiplication because well we cant since ac is a string lol
    p1 = padZeros(str(ac), p1Pad, False)
    #doing the (a+b)(c+d) - ac - bd portion over a few lines.
    t1 = subtractStrings(temp, ac)
    t2 = subtractStrings(t1, bd)
    #doing bit shift to maintain proper precision (10^(n/2))
    p2 = padZeros(t2, p2Pad, False)
    #finally adding it all up and questioning my will to continue
    ans = addStrings(p1, p2)
    ans = addStrings(ans, bd)
    #This removes any leading zeros because we don't want those!
    tempAns = ""
    if len(ans) > 1 and ans[0] == '0':
        i = 0
        while i < len(ans) and ans[i] == '0':
            i+=1
        while i != len(ans):
            tempAns = tempAns + str(ans[i])
            i+=1
    else:
        tempAns = ans
    return tempAns

def gradeSchool(x, y):
    x = str(x)
    y = str(y)
    numZeros = 0
    sum = ""
    #make sure each string is of equal length
    if len(x) < len(y):
        x = padZeros(x, len(y) - len(x), True)
    elif len(y) < len(x):
        y = padZeros(y, len(x) - len(y), True)

    #loop through first number
    for i in range(len(x)-1, -1, -1):
        #cant forget that big boi carry
        carry = 0
        #gotta track the sum
        tempSum = ""
        #add 1 zero for each degree of precision in the 2nd number ish
        # there will be len(y)-1 zeros added to the last one
        tempSum = padZeros(tempSum, numZeros, False)
        #loop through second number
        for j in range(len(y)-1,-1,-1):
            #multiply ONE digit at a time that way max value of the int can be 9*9+maxCarryOf8 = 89
            #therefor the highest int used here will be 89 which will never cause an overflow
            tt = int(x[i]) * int(y[j])
            tt += carry
            tt = str(tt)
            # if tt is bigger than 1 digit then we need to separate the carry
            # this does that nicely
            if len(tt) > 1 :
                carry = int(tt[0])
            else:
                carry = 0
            # This keeps tally of the tempSum
            # if there was a carry this ensures it gets the 2nd digit but also wont be out of bounds
            # in the case that there is no carry
            tempSum = tt[len(tt)-1] + tempSum
        #outside the inner for loop this is used to grab any left over carrys. wouldnt want anyone feeling left out now
        if carry > 0:
            tempSum = str(carry) + tempSum
        #keep a running sum of what you've got so far as your traverse deeper and deeper into the fun exciting
        #grade school multiplication algorithm
        sum = addStrings(sum, tempSum)
        numZeros += 1

    tempAns = ""
    if len(sum) > 1 and sum[0] == '0':
        i = 0
        while i < len(sum) and sum[i] == '0':
            i+=1
        while i != len(sum):
            tempAns = tempAns + str(sum[i])
            i+=1
    else:
        tempAns = sum
    return tempAns

def extraCredit():
    xAxis = np.array(0)
    gradeSchoolTimes = np.array(0)
    karatsubaTimes = np.array(0)
    A = 999
    logBase10ofA = 2.99956548823
    print("Performing exponentiation using dec by constant, with karatsubas and gradeschool. this will take a while")
    for i in range(9, 2300, 200):
        print("working on b of: ", i)
        start = time.time()
        decByConsWithGradeSchool(A, i)
        end = time.time()
        gradeSchoolTimes = np.append(gradeSchoolTimes, end - start)

        start = time.time()
        decByCons(A, i)
        end = time.time()
        karatsubaTimes = np.append(karatsubaTimes, end - start)

        xAxis = np.append(xAxis, logBase10ofA * i)

    gradeSchoolTimes = np.delete(gradeSchoolTimes, 0)
    karatsubaTimes = np.delete(karatsubaTimes, 0)
    xAxis = np.delete(xAxis, 0)

    mpl.style.use('seaborn')
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(gradeSchoolTimes) * 1.1)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    ax.get_yaxis().get_major_formatter().set_scientific(False)

    timesVsN = plt.figure(1)
    plt.xlabel('Size of n where n = b*log_10(a)')
    plt.ylabel('Time to Compute A^B in seconds')
    plt.title('Extra Credit')
    plt.plot(xAxis, karatsubaTimes, '.g-', color="green", linewidth=1, label="karatsuba")
    plt.plot(xAxis, gradeSchoolTimes, '.r-', color="red",linewidth=1, label="grade school")
    plt.legend(loc="upper left")

    plt.show()

run = True
while run:
    modeBool = False
    while modeBool == False:
        mode = input("Please enter 'Task1', 'Task2', 'ExtraCredit', or 'Quit': ")
        if mode == 'Task1':
            aEntered = False
            while aEntered == False:
                A = input("Please enter an integer A between 1 and 1000: ")
                if int(A) < 1 or int(A) > 1000:
                    print("That was not a correct A value input try again")
                else:
                    aEntered = True
            bEntered = False
            while bEntered == False:
                B = input("Please enter an integer B between 1 and 1000: ")
                if int(B) < 1 or int(B) > 1000:
                    print("That was not a correct B value input try again")
                else:
                    bEntered = True
            print(A, " * ", B, " = ", karatsuba(A, B))
            modeBool = True
        elif mode == 'Task2':
            aEntered = False
            while aEntered == False:
                A = input("Please enter an integer A between 1 and 1000: ")
                if int(A) < 1 or int(A) > 1000:
                    print("That was not a correct A value input try again")
                else:
                    aEntered = True
            bEntered = False
            while bEntered == False:
                B = input("Please enter an integer B between 1 and 1000: ")
                if int(B) < 1 or int(B) > 1000:
                    print("That was not a correct B value input try again")
                else:
                    bEntered = True
            print(A, " raised to the power of ", B, " = ", decByCons(int(A), int(B)))
            modeBool = True
        elif mode == 'ExtraCredit':
            extraCredit()
            modeBool = True
        elif mode == 'Quit':
            modeBool = True
            run = False
            break
        else:
            print("Incorrect mode input, please try again. Make sure you leave out the single quotes")



#############################################################################
#############THIS WAS ALL TEST STUFF AND SOME FOR FUNZIES STUFF##############
#############################################################################
#extraCredit()
#
#start = time.time()
#t = decByConsWithGradeSchool(999,999)
#end = time.time()
##print("gradeSchool = ", t)
#print("Calculated in: ", end - start, " using grade school algorithm")
#
#start = time.time()
#l = decByCons(999,999)
#end = time.time()
##print("karatsuba = ", l)
#print("Calculated in: ", end - start, " using karatsubas algorithm")

#print(karatsuba(2101, 1130))
#print(karatsuba(88,4))
#start = time.time()
##print(karatsuba(1000, 1000))
#print(karatsuba(12789362103761212323123547345234341231231233, 123712365912351342222222222222222222234551235765734542352348123))
#end = time.time()
#print("Calculated in: ", end - start)
#
#158220224524698074883437259708693019449692034261706775659
#158220224524698074883437259708693019449692034261706775659
#print(decByCons(1000,1000))
#t = str(decByCons(1000,1000))
#count = 0
#for i in t:
#    count += 1
#print(count)
#
#
#
#y = "0"
#x = "239"
#print(addStrings(y, x))
#print(subtractStrings(y, x))
#print(karatsuba(x, y), " kara?")
#print(gradeSchool(x, y))

#This was used to test the accuracy of my karatsuba vs gradeschool vs python
#for i in range(1,1000):
#    for j in range(1,1000):
#        temp1 = karatsuba(str(i),str(j))
#        temp2 = i * j
#        temp3 = gradeSchool(str(i), str(j))
#        if int(temp1) != temp2 or int(temp3) != temp2:
#            print("broke on i, j: ", i, j)
#            print("temp1: ", temp1, "temp2: ", temp2)
#
#        else:
#            print("good?")
#

#had some funky problems with subtraction but this helped me fix it!
#for i in range(1,800):
#    for j in range(1,800):
#        temp1 = subtractStrings(i, j)
#        temp2 = 0
#        if i < j:
#            temp2 = j - i
#        elif j < i:
#            temp2 = i - j
#        if int(temp1) != temp2:
#            print("broke on i, j", i, j)
#            print("temp1: ", temp1, " temp2: ", temp2)
#        else:
#            print("all good")