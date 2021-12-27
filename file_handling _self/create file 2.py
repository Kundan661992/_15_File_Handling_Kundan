file = open("write_data1.txt", 'w')
print("File type ", file, type(file))
data = input('Enter text : ')
file.write(data)
file.close()
print(' the fie is completed')

a = open("write_data.txt", 'w')
print("File type ", a, type(a))
print('\n')
data = input("Enter data here : ")
a.write(data)

f = open('abc.txt', 'w')
print('File Name: ', f.name)
print('File Mode: ', f.mode)
print('Is File readable: ', f.readable())
print('Is File writable: ', f.writable())
print('Is File closed : ', f.closed)
f.close()
print('Is File Closed : ', f.closed)

# Writing data to text files:
# We can write character data to the text files by using the following 2 methods.
# write(str)
# writelines(list of lines)

f = open('abcd.txt', 'w')
f.write('Kundan\n')
f.write('Kumar\n')
f.write('Singh\n')
print('Data written to the file successfully')
f.close()

# Note: In the above program, data present in the file will be overridden everytime if we
# run the program. Instead of overriding if we want append operation then we should open
# the file as follows.
f = open('abcd.txt', "a")
f = open('abcd.txt', 'w')
list = ['sunny\n', "bunny\n", 'vinny\n', 'chinny']
f.writelines(list)
print('List of lines written to the file successfully')
f.close()

# compulsory we have to provide line seperator(\n),otherwise total data should be written to a single line.


# Reading Character Data from text files:
# We can read character data from text file by using the following read methods.
# read()-- To read total data from the file
# read(n) -- To read 'n' characters from the file
# readline()-- To read only one line
# readlines()-- To read all lines into a list
# Eg : To read total data from the file


# Eg 1: To read total data from the file
f = open('abc.txt', 'r')
data = f.read()
print(data)
f.close()

# Eg 2: To read only first 10 characters:
f = open('abc.txt', 'r')
data = f.read(10)
print(data)
f.close()

# Eg 3: To read data line by line:
f = open('abc.txt', 'r')
line1 = f.readline()
print(line1, end='')
line2 = f.readline()
print(line2, end='')
line3 = f.readline()
print(line3, end='')
f.close()

# Eg 4: To read all lines into list:
f = open('abc.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()

# Eg 5:
f = open('abc.txt', 'r')
print(f.read(3))
print(f.readline())
print(f.read(4))
print('Remaining data')
print(f.read())

# Eg:
with open('abc.txt', 'w') as f:
    f.write('Kudan\n')
f.write('Kumar\n')
f.write('Singh\n')
print('Is File Closed: ', f.closed)
print('Is File Closed: ', f.closed)

# The seek() and tell() methods:
# tell():
# == We can use tell() method to return current position of the cursor(file pointer) from
# beginning of the file. [ can you plese telll current cursor position]
# The position(index) of first character in files is zero just like string index.
# Eg:
f = open('abc.txt', 'r')
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())

# seek():
# We can use seek() method to move cursor(file pointer) to specified location.
# [Can you please seek the cursor to a particular location]
# f.seek(offset, fromwhere)


data = 'All Students are STUPIDS'
f = open('abc.txt', 'w')
f.write(data)
with open('abc.txt', 'r+') as f:
    text = f.read()
    print(text)
    print('The Current Cursor Position: ', f.tell())
    f.seek(17)
    print('The Current Cursor Position: ', f.tell())
    f.write('GEMS!!!')
    f.seek(0)
    text = f.read()
    print('Data after modification:')
    print(text)



# a file is present or not
import os,sys
fname=input('Enter file Name: ')
if os.path.isfile(fname):
    print('File exists:',fname)
    f=open(fname,'r')
else:
    print('File does not exist:',fname)
    sys.exit(0)
print('The content of file is:')
data=f.read()
print(data)