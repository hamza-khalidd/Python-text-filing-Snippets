# write data in a file.
file1 = open("myfile.txt", "w")
L = ["Python \n", "Programming \n", "Language \n"]

file1.write("Hello \n") #Write 1 Line
file1.writelines(L) #Write Multiple Lines
file1.close()