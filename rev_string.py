# program to reverse a string
name = input('enter a name')
print('entered name is:',name)
'''print(name[start:end])'''# using slice
# print(name[::-1])

reverse = ""
for i in name:
    #print(i)
    reverse = i + reverse
print('Reversed value of {} is {}'.format(name,reverse))    