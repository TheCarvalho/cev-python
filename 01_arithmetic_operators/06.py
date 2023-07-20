
# *ex6 = Create an algorithm that reads a number and displays its double, triple, and square root.

num = int(input("Enter a number: "))

print(
    'The double of your number is: {}\nThe triple is: {}\n'
    'The square root is: {:.2f}'.format(num * 2, num * 3, num ** (1/2))
)
