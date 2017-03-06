with open("with_example.txt",'a+') as file:
    file.seek(0)
    content=file.read()
    file.write("\nLine 6")
    print(file)
