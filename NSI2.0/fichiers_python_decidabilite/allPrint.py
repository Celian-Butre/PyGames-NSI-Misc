file = 'file_1_OK.py'
isAllPrint = True
with open(file) as f:
    for line in f:
        text = line
        if text != '\n' and text[0] != '#' and text[0:5] != 'print':
            print(line)
            isAllPrint = False
print(isAllPrint)