import re
with open('myfile.txt', 'r+') as f:
    text = f.read()
    text = re.sub('Hello', 'Hello world', text)
    f.seek(0)
    f.write(text)
    f.truncate()