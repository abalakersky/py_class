import datetime

filename = datetime.datetime.now()

def create_file():
    with open(filename.strftime("%Y-%m-%d_%H-%M-%S")+".txt", 'w') as file:
        file.write("")

create_file()
