#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
START_TXT = "Last digit of"
lastTxt = 'and is 0'

if number < 0:
    lastDigit = lastDigit * -1
if (lastDigit < 6) & (lastDigit != 0):
    lastTxt = "and is less than 6 and not 0"
elif lastDigit > 5:
    lastTxt = "and is greater than 5"

print(f"{START_TXT} {number} is {lastDigit} {lastTxt}")
