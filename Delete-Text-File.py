import os
if os.path.exists("filename.txt"):
  os.remove("filename.txt")
else:
  print("The file does not exist")