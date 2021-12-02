import io

f = open('./input1','r')
prevline = -1
linecount = 0
count = 0
with open('./input1','r') as f:
    for lines in f:
        linecount += 1
        line = lines.strip('\n')
        line = int(line)
        if prevline != -1:
            if line < prevline:
                print('decreasing', line)
            elif line > prevline:
                print('increasing', line)
                count += 1
            else:
                print('same')
        else:
            print('n/a')
        prevline = line
print('increasing count: ', count)
f.close()