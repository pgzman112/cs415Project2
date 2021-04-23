Preston Zimmerman
Diana acre
4/6/2021
Project 2b

Preliminary Note: I used strings to hold numbers. Strings are character arrays. strings were just nice to work with
for easy appending. like str1 + str2 = them concatinated ect. but the main thing is that strings are character arrays so by default I am
using an array, it just happens to be immutatable in python which turns out to be very annoying later in the project. I really should have done it in c++
except that it would have made the graphing portion harder.

The reason I immdiately went with strings is because that's what I used when I did the pretty much same assignment in 460 last semester so it was fresh
in my mind doing this with strings. (not exactly the same project, we built a real number library to handle arbitrary precision that allowed integer and decimal addition,
subtraction, multiplication, and division up to 256 digits on both sides of the decimal place)

steps to run this program
1) open new python project in pycharm and place the karatsuba.py file inside of it.
2) Go into settings for your current python project and click on python interpreter.
3) make sure python 3.9 is being used (others should work but I am on 3.9)
    - Then click the + arrow at the bottom and make sure you import numpy and matplotlib
4) Once interpreter is setup we need to create a run config
    - in the upper right click edit configurations, click the plus to create a new python run config
    - Set script path to the correct directory ending with -> karatsuba.py
    - click the play button. This one should be very easy to setup.


EXTRA CREDIT
I know you wanted 999^9 -> 999^999 but I thought it looked better going higher, it does take longer to
run so I will include an image of my output after running it on A of 999 and B in range (9, 2209) (incrementing by 200).
I just thought this graph gave a much better picture. They are roughly even up until an n value of ~2500
where n is B*log_10(A). after a b value of 809 there is a clear shift to karatsuba being faster than gradschool
for multiplication.

I think my karatsuba implementation could be more efficient than it is because sometimes it has
to remove a lot of leading zeros which slows it down. But im not getting paid and I don't
really care that much. Then again both my karatsuba and grade school implementation have to remove leading zeros.

SAMPLE OUTPUTS:
    Task1/Task2:
        Please enter 'Task1', 'Task2', 'ExtraCredit', or 'Quit': Task1
        Please enter an integer A between 1 and 1000: 100
        Please enter an integer B between 1 and 1000: 21
        100  *  21  =  2100
        Please enter 'Task1', 'Task2', 'ExtraCredit', or 'Quit': Task2
        Please enter an integer A between 1 and 1000: 5
        Please enter an integer B between 1 and 1000: 10
        5  raised to the power of  10  =  9765625
        Please enter 'Task1', 'Task2', 'ExtraCredit', or 'Quit': Quit
