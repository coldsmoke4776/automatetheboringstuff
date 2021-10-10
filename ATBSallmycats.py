# Write your code here :-)
catNames = [] #assigning an empty list ready to store the cat names
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop):') #user prompt
    name = input() #user can enter the name of the cat
    if name == '':
        break #function to allow user to quit cleanly
    catNames = catNames + [name] #list concatenation
print('The cat names are: ')
for name in catNames:
    print('  ' + name)
