import random
import math
import os
import sys
from math import gcd
import time
coprime = 0
cofactor = 0
TimesGenerated = 0
while True:
    try:
        TimesToGenerate = int(input("How many trials would you like to run? The more trials, the more time this will take, but the more accurate it will become. "))
        break
    except ValueError:
        print("Please input a valid integer.")
while True:
    random.seed
    int1 = random.randint(1,1000000000000000000000000)
    int2 = random.randint(1,1000000000000000000000000)
    if gcd(int1,int2) == 1:
        coprime = coprime + 1
        TimesGenerated = TimesGenerated + 1
    else:
        cofactor = cofactor + 1
        TimesGenerated = TimesGenerated + 1
    if TimesGenerated == TimesToGenerate:
        odds = coprime/(cofactor+coprime)
        pie = math.sqrt(6/odds)
        print("Pi: " + str(pie))
        percent_error = abs((math.pi - pie)/math.pi) * 100
        print("Percent error: " + str(percent_error) + "%")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 