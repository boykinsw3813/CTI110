#RandomNumberWriter
#7/17/17
#CTI-110 M6HW1 -RandomNumberFileWriter
#Boykins William
#

import random

randfile = open('randomFile.txt','w')

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1,500)) + "\n"
    randfile.write(line)
    print(line)

randfile.close()
