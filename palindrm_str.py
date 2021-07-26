# program to check  a string is palindrome or not
# eg:  madam,level,mom
name = input('Enter a string or name:')
print('original string:',name)
reversedvalue = name[::-1]
print('reversed string:',reversedvalue)

if(name==reversedvalue):
    print('it is palindrome')
else: 
  print('it is not a palindrome')