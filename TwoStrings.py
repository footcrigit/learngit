#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):


    for i in s2:
        k = s1.find(i)
        if k > 0:
            return 'Yes'

    return 'No'


q = 1

for q_itr in range(q):
    s1 = 'hi'

    s2 = 'hello'

    result = twoStrings(s1, s2)
    print(result)

