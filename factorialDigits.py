#Given a number. returns the number of digits of the factorial.
#Formula Source: https://math.stackexchange.com/questions/661227/factorial-length
import math

def factorialDigits(n):
    if n != 0:
        return math.floor((math.log(2*math.pi*n)/2+n*(math.log(n)-1))/math.log(10))+1
    else:
        return 0