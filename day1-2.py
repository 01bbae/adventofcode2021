import io

f = open('./input1','r')

windowsize = 3
counter = 0
sum = 0
with open('./input1','r') as f:
    for lines in f:
        line = lines.strip('\n')
        line = int(line)
        sum += line
        

        
f.close()



#take sum of window
#if sum is sum of 4 elements subtract first element
#if sum is 1 element record firstelem
#if sum is 2 elements skip
#if sum is 3 elements skip