x = str(input('Enter the text: '))
t = 0
for i in x:
    if i == 'a' or i == 'A':
        x.replace('a', ' ')
        t += 1
print(t)
