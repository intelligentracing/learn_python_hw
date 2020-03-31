import os

source_filename = 'nasdaqetfs.txt'
result_filename = 'nasdaqesorted.txt'

try:
    # Obtain current python file's path
    path = os.path.dirname(os.path.abspath(__file__))
    # Open source file and the result file
    source_handle = open(path+'/'+source_filename,'r')
    result_handle = open(path+'/'+result_filename,'w')
    result_list=[]
    for line in source_handle:
        line= list(line)
        start=0
        end=0
        temp=[]
        for i in range(len(line)):
            if line[i]=="|" and start==0 and end==0:
                start=i
            elif line[i]=="|" and start!=0 and end==0:
                end=i
            else:
                continue
        for k in range(start+1,end):
            temp.append(line[k])
        temp="".join(temp)
        result_list.append(temp)
    result_list=sorted(result_list)
    for j in result_list:
        result_handle.write(j)
        result_handle.write("\n")
except IOError:
    print('IO Error! Please check valid file names and paths')
    exit
finally:
    source_handle.close()
    result_handle.close()
