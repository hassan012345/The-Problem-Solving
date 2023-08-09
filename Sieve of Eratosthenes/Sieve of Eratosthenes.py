# Sieve of Eratosthenes
#Make a list of all number upto given number.
#Mark 2 i.e the first number as prime and cross out its multiples.
#Mark the next number as prime and cross out its multiples.

from math import floor, sqrt


def sieve_of_eratosthenes(max_num):
    numbers = {}
    for i in range(2,max_num+1):
        numbers[i] = "Prime"
    multiples = []
    for j in range(2,int(sqrt(max_num)+1)):
        if j not in multiples:
            curr_prime = j
            for k in range(2*j,max_num,j):
                if k not in multiples:
                    multiples.append(k)
    for p in range(0,len(multiples)):
        numbers[multiples[p]] = "Not Prime"
    return numbers
print(sieve_of_eratosthenes(5))