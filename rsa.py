#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa.py
# description: RSA
# Jaxon Willard
# A02088218
##############################################################


import numpy as np
from rsa_aux import xgcd, mod_exp
from rsa_aux import mult_inv, euler_phi, is_prime
import math
import random

class rsa(object):

    ### Assign 12, subproblem 1.5
    @staticmethod
    def choose_e(eu_phi_n):
        ### your code here
        lwr = 11
        nums = []
        for i in range(lwr, eu_phi_n-1):
          if (xgcd(i,eu_phi_n)[0] == 1):
            nums.append(i)

        return nums[random.randint(0, len(nums)-1)]

        pass

    ### Assign 12, subproblem 1.6
    @staticmethod
    def generate_keys_from_pqe(p, q, e):
        ### your code here
        
        n = p*q
        d = mult_inv(e,n)
        return ((e,n), (mult_inv(e,(p-1)*(q-1)), n))

        

    ### Assign 12, subproblem 1.7    
    @staticmethod
    def encrypt(m, pk):
        ### your code here
        pass

    ### Assign 12, subproblem 1.7        
    @staticmethod
    def decrypt(c, sk):
        ### your code here
        pass

    ### Assign 12, subproblem 1.8
    @staticmethod
    def encrypt_text(text, pub_key):
        ### your code here
        pass

    ### Assign 12, subproblem 1.8        
    @staticmethod    
    def decrypt_cryptotexts(cryptotexts, sec_key):
        ### your code here
        pass
