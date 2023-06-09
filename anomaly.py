
#import math/statistics functions
from statistics import mean
from statistics import stdev

#this function returns the ith column in a 2D list A
def get_col(A, i):
    return [float(row[i]) for row in A]

#==============================================================

#open the file
f = open("mammal_sleep_1.txt")

#read the file into a matrix
lines = [line.rstrip().split("\t") for line in f]

#get each column (attribute) in the matrix
for i in range ( 1, len(lines[0])):

    #extract all the attribute values into an array x
    x = get_col(lines, i)
    
    #compute mean
    m = mean(x)
    
    #compute stdev
    s = stdev(x)
    
    #for each entry in x, check whether it is an anomaly, print anomalous values.
    for v in x:
        if v > (m + (2*s)) or v < (m - (2*s)):
            print (v)

#close the file
f.close()


