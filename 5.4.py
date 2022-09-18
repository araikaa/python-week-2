x= str(input('Enter the text: '))
count = 0
for i in x:
    if i == 'x':
        x=x.replace('a', 'o')
        count += 1
print(count)
