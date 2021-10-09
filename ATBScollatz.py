# Write your code here :-)
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

try:
    number = input('Enter a number:')
    while number != 1:
            number = collatz(int(number))
except ValueError:
    print('Must enter an integer')

