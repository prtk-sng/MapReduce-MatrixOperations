#!/usr/bin/env python3
import sys

# arguments to support the matrix's size.
M_row = int(sys.argv[1])
M_col = int(sys.argv[2])
N_row = int(sys.argv[3])
N_col = int(sys.argv[4])
X_row = int(sys.argv[5])
X_col = int(sys.argv[6])

# code to obtain the indices given the size of input matrices
i = [val for val in range(M_row)]
j = [val for val in range(N_col)]
x = [val for val in range(M_col)]

Xij=[[x,y] for x in i for y in j] # indices based on the size of input matrices

'''
The code chunks below emits the key values pairs for the input matrices M,N,and X.
The format of the key value pairs is k1,k2,k3,V.
For instance, if values V1 and V2 are consistent with all three keys, then V1 & V2 are multiplied.
k1,k2 corresponds to the indices of the resulting output matrix in the reducer and therefore values
with same k1,k2 are summed up to obtain the expected result.
'''

for line in sys.stdin:
    if line.strip() != '': 
        line = line.strip() # To ignore the ending whitespace in the output
        ele = line.split(", ") # splitting into an array

        if ele[0]=='1' : # code to emit key value pairs for the matrix M
            for idx in x:
                for idx_i in j :
                    indices = '\t'.join(map(str, Xij[idx_i + int(ele[1])*N_col]))
                    print('{0}\t{1}\t{2}'.format(indices, idx, ele[2+idx])) # Emit Key value pairs

        elif ele[0]=='2' : # code to emit key value pairs for the matrix N
            for idx in j:
                for idx_i in i :
                    indices = '\t'.join(map(str, Xij[idx + int(idx_i)*N_col]))
                    print('{0}\t{1}\t{2}'.format(indices, ele[1], ele[2+idx])) # Emit Key value pairs

        elif ele[0]=='3' : # code to emit key value pairs for the matrix X
            for idx in j:
                indices = '\t'.join(map(str, Xij[idx+ int(ele[1])*N_col]))
                print('{0}\t{1}\t{2}'.format(indices, 'X', '-'+ele[2+idx])) # Emit Key value pairs