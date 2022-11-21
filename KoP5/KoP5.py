import random
import numpy as np

rows = 3
column = 10

array = np.random.randint(-1000000,1000000,size = (rows,column))

array[rows-1] = np.sort(array,axis=1)[rows-1]

print(array)

print(np.median(array[rows-1]))

if array.shape[1]%2 != 0:
    print(array[rows-1,array.shape[1]//2])
else:
    print((array[rows-1,array.shape[1]//2-1]+array[rows-1,array.shape[1]//2])/2)

##Результаты счёта##
"""
    [[ 569678 -427582  528624 -688920  985568 -252491  -23370   37281 -493566 -996283]
    [ 432859 -369418 -887552 -838383   49161 -464170  405259 -793088  170109 188813]
    [-903284 -850274 -771495 -698475 -474915 -320097  671378  803503  873900 942214]]
    -397506.0
    -397506.0
"""