#!/usr/bin/env python3
import sys

# empty dictionaries to store sum and product based on input key value pairs.
sum = {}
prod = {}

for line in sys.stdin:
    line = line.strip()
    k1,k2,k3,num = line.split('\t')
    
    if (k1,k2,k3) in prod.keys(): # multiply if already present in the dictionary
        prod[k1,k2,k3] = int(prod[k1,k2,k3])*int(num)
        if (k1,k2) in sum.keys():
            sum[k1,k2] = int(sum[k1,k2])+int(prod[k1,k2,k3])
        else:
            sum[k1,k2] = int(prod[k1,k2,k3])

    else: # adding a new key to the dictionary
        prod[k1,k2,k3] = int(num)
        if k3 == 'X':
            if (k1,k2) in sum.keys():
                sum[k1,k2] = int(sum[k1,k2])+int(prod[k1,k2,k3])
            else:
                sum[k1,k2] = int(prod[k1,k2,k3])

for indices in sorted(sum.keys()):
    print('{0}\t{1}\t{2}'.format(indices[0], indices[1], (-1)*sum[indices])) # emit the final output