myFile = open('filename.txt', 'rt', encoding='utf8')
print(myFile.read())
myFile = open('filename.txt', 'rt', encoding='utf8')
for line in myFile:
    print(line)
myFile = open('filename.txt', 'rt', encoding='utf8')
print(myFile.readlines())