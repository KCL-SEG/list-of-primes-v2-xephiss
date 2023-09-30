"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'Error: Input value: {number_of_primes} is less than 1.')
    elif number_of_primes % int(number_of_primes) != 0:
        raise ValueError(f'Error: Input value: {number_of_primes} is not an integer')
    else:
        primeList = [2]
        next = 3
        while len(primeList) != number_of_primes:
            addNumberToList(next, primeList)
            next += 1
        return primeList


def addNumberToList(number, primeList):
    for i in primeList:
        if number % i == 0:
            return False
    primeList.append(number)
