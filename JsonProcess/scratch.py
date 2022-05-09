import json
import os
import re


with open('scratch_test123.json', 'r') as file:
    res = []
    res = file.readlines()
    n = len(res)
with open('weather_condition.json', "w") as resfile:
    resfile.write('[')
    for i in range(0,n-1):
        resfile.write(res[i]+',')
    resfile.write(res[n-1]+']')

