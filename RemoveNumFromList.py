import re

def remove(list):
    pattern = '[0-9]'
    pattern1 = '\n'
    list = [re.sub(pattern, '', i) for i in list]
    list = [re.sub(pattern1, '', i) for i in list]
    return list

text_file = open(r"C:\Users\count\RemoveNum.py\testfile.txt", "r")

list1 = text_file.readlines()

your_data = remove(list1)

#print(*your_data, sep = "\n")

print(*your_data, sep = "\n", file=open(r"C:\Users\count\RemoveNum.py\output.txt","w"))






