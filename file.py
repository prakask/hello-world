import sys
tfile = open("module1.txt","w+")
print tfile.mode
print tfile.name
for i in range(1,1000):
    tfile.write("This is a string that i am writing into the file This is a string that i am writing into the fileThis is a string that i am writing into the fileThis is a string that i am writing into the fileThis is a string that i am writing into the fileThis is a string that i am writing into the fileThis is a string that i am writing into the fileThis is a string that i am writing into the fileThis is a string that i am writing into the file\n")
tfile.close()

rfile=open("module1.txt","r")
print rfile.read()
rfile.close()
    
