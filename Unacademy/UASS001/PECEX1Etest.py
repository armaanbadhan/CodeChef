import sys
import random
 
n = 2
 
def n_mod_x(x):
    global n
    if x < 1 or x > 2 * (10 ** 18):
        print('Wrong Answer')
        print('Given number out of range, when hidden number = ', n)
        exit()
    return n % x
 
# ----------------------------------------------------------------------------------------------------------------
 
# The following function always returns 0, you should complete it so that it returns the hidden value always
# You can call n_mod_x upto 150 times
def guess():
    return n_mod_x(int(2e18))
 
 
# ----------------------------------------------------------------------------------------------------------------
 
T = 100
while T > 0:
    n = random.randint(2, 10 ** 18)
    guessed = guess()
    if guessed != n:
        print('Wrong Answer!')
        print('When hidden number = ', n, ' guessed number = ', guessed)
        exit()
    x = (guessed == guess())
    assert(x)
    print('Correct when hidden number = ', n)
    T-= 1
print('ok')
 