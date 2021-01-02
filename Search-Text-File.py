strr = 'Python'
with open('myfile.txt') as f:
    if strr in f.read():
        print("String Found")
    else:
        print("String Not Found")