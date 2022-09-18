x = str(input('Enter the text: '))
for i in x.split():
    if i.count('a') == True:
        if i.endswith('i') == True:
            print(i)
