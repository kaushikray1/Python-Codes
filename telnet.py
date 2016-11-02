# I wrote this small script to verify the robustness for ESP-Link firmware over Wifi using a LoopBack configaration (Rx tied to TX)


import getpass
import sys
import telnetlib
import time 
import StringIO
import random
import array
import string


val = 100
itte = 200000000
PROMPT = ']'

list_1 = [random.randrange(65,90) for c in range(val)]
list_1.insert(val, ']')
str2 = ''.join(str(e) for e in list_1)

HOST = "192.168.2.235"

tn = telnetlib.Telnet(HOST,23)

count = 0
error = 0
while count<itte:
    tn.write("%s" %str2)
    str1 = tn.read_until(PROMPT,5)
    count = count + 1
    if str1 != str2:
       error = error + 1
       tn.read_until(PROMPT,1)
    if count % 100 == 0:
        print count, 
        print " ",
        print error
    
print ("\nTotal number of errors out of 2000 are: %i"  %error)    
tn.close
