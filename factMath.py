import math

#Given a number n, returns y, with y being the exponent of 10, such that 10^y = n! (n factorial)
def factLog10(n):
    if n!=0:
        return (math.log(2*math.pi*n)/2+n*(math.log(n)-1))/math.log(10)
    else:
        return 0

#Given a number n. returns the number of digits of n factorial.
#Formula Source: https://math.stackexchange.com/questions/661227/factorial-length
#Modified to depend on the factLog10 algorithn
#Instead of doing math.floor(something)+1, math.ceil(something) is done instead. This yields the same result.
def factorialDigits(n):
    return math.ceil(factLog10(n))