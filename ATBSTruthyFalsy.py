# Write your code here
name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numofGuests = int(input())
if numofGuests:
    print('Be sure to have enough room for everyone!')
print('Done')
