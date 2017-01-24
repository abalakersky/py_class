
import glob2
import datetime

filelist = glob2.glob('file*.txt') 
filename = datetime.datetime.now()

def create_file():
    with open(filename.strftime("%Y-%m-%d_%H-%M-%S")+".txt", 'w') as file:
        for f in filelist:
            with open(f,'r') as oldFile:
                file.write(oldFile.read()+"\n")
            # oldFile = open(f,'r')
            # content = oldFile.read()
            # file.write(content+'\n')
            # oldFile.close()

create_file()
