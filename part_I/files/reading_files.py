# make sure you’ve created the file from the previous example

with open("my_file.txt", "r") as my_file:
    for line in my_file.read():
        print(line)
