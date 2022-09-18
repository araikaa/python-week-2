x = str(input('Enter the text: '))
t = 1
t = 0
for i in x:
    if i == ' ':
        a = x.split(' ')
        t += 1
print(t)
