file = open("example.txt",'r') #Open file in read mode
type(file) #Check type of file object
content = file.read() # read contents of the file into content var
print(content) # print contents of content
print(file) # print file object
content = file.readlines() # read contents using readlines
print(content) # print content again. it is empty because read pointer is at the end of the file from the first read operation
file.seek(0) # move read pointer to begining of file 0
content = file.readlines() # readlines again
print(content) # print list of lines with \n added to each item of the list
content=[i.rstrip("\n") for i in content] # strip \n from each item in place.
print(content) # print content again
file.close() # close file
