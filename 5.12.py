x = str(input('Enter the text: '))
a = ''
for i in x.split():
    if i.endswith('i'):
        print(i, " ")
