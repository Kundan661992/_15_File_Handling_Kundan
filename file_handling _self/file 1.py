"""

                                File Handling
As the part of programming requirement, we have to store our data permanently for future purpose.
For this requirement we should go for files.Files are very common permanent storage areas to store our data.

Advantages of storing data in file: cronjob
------------------------------------
 - Data can be stored permanently
 - We can update the data in file whenever required
 - File can be shared to multiple users when required
 - To store huge amount of data, files are very helpful



                                Types of Files:
There are 2 types of files

1. Text Files:
Usually we can use text files to store character data
eg: abc.txt

2. Binary Files:
Usually we can use binary files to store binary data like images,video files, audio files etc...





Opening a File:

Before performing any operation (like read or write) on the file,first we have to open that file.
For this we should use Python's inbuilt function open()But at the time of open, we have to specify mode,
which represents the purpose of opening file.
f = open(filename, mode)

The allowed modes in Python are

1. r -- open an existing file for read operation. The file pointer is positioned at the beginning of the file.
If the specified file does not exist then we will get

FileNotFoundError.This is default mode

2. w -- open an existing file for write operation. If the file already contains some data then it will be overridden.
       If the specified file is not already available then this mode will create that file.

3. a -- open an existing file for append operation. It won't override existing data.If the specified file is not
already avaialble then this mode will create a new file.

4. r+ -- To read and write data into the file. The previous data in the file will not be deleted.
The file pointer is placed at the beginning of the file.

5. w+ -- To write and read data. It will override existing data.

6. a+ -- To append and read data from the file.It wont override existing data.

7. x -- To open a file in exclusive creation mode for write operation. If the file already exists then we will
get FileExistsError.

Closing a File:

After completing our operations on the file,it is highly recommended to close the file.For this we have to
use close() function.
f.close()


                     Various properties of File Object:

Once we opened a file and we got file object,we can get various details related to that file by using its properties.

name -- Name of opened file
mode -- Mode in which the file is opened
closed -- Returns boolean value indicates that file is closed or not
readable() -- Returns boolean value indicates that whether file is readable or not
writable() -- Returns boolean value indicates that whether file is writable or not.





                                         The with statement:
The with statement can be used while opening file.We can use this to group file operation statements within a block.
The advantage of with statement is it will take care closing of file,after completing all operations
automatically even in the case of exceptions also, and we are not required to close explicitly.


                      a particular file exists or not?
We can use os library to get information about files in our computer.os module has path sub module,which
contains isFile() function to check whether a particular file exists or not?
os.path.isfile(fname)
"""