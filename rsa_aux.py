#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa_aux.py
# description: auxiliay functions for RSA
# Jaxon Willard
# A02088218
##############################################################

import numpy as np
import math

### Assign 12, subproblem 1.1
def xgcd(a,b):
    ''' 
    extended gcd that returns d, x, y such that
    d = ax + by.
    '''
    prevx, x, = 1, 0
    prevy, y, = 0, 1
    aa, bb = a, b
    while bb != 0:
        q = aa // bb
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        aa, bb = bb, aa % bb
    return aa, prevx, prevy

### Assign 12, subproblem 1.2
def mult_inv(a, n):
    """
    multiplicative inverse of a in Z^{*}_{n}.
    """
    b = 0
    while True:
        if (a*b-1) % n == 0: return b
        b +=1


### A tool you may want to use in your code.
### it's used in rsa_uts.py.
def z_star_sub_n(n):
    """
    compute the elements of Z^{*}_{n}.
    """
    return np.array([i for i in range(n) if xgcd(i, n)[0] == 1])

### A tool you may want to use in your code (e.g., euler's totient)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 2:
        for d in range(3, int(math.floor(math.sqrt(n)))+1, 2):
            if n % d == 0:
                return False
        return True

### A tool you may want to use in your tests (e.g., euler's totient)
def find_primes_in_range(a, b):
    return [i for i in range(a, b+1) if is_prime(i)]


### Assign 12, subproblem 1.3.
def mod_exp(a, b, n):
    """
    this function computes a^b mod n.
    """
    return a ** b % n
    # c = 0
    # d = 1
    # binRep = bin(b)[2:]
    # for i in reversed(binRep):
    #   print('i', i)
    #   c = 2 * c
    #   d = d * d % n
    #   if i == 1:
    #     c = c + 1
    #     d = d * a % n
    # print(a ** b % n, d)
    # return d


### Assign 12, subproblem 1.4
def euler_phi(n):
    """ Euler's Totient """
    primes = []
    for i in range(2,n+1):
      prime = True
      for j in range(1,i):
        if xgcd(i,j)[0] != 1:
          prime = False
          break
      if prime and n % i == 0:
        primes.append(i)

    phi = n
    for prime in primes:
      phi *= (1 - (1 / prime))
    
    return int(phi) 

    

    

