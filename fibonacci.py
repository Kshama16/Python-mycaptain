Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Prompt user for how many Fibonacci numbers to generate
... n = int(input("How many Fibonacci numbers do you want to generate? "))
... 
... # Initialize variables for the first two numbers in the sequence
... fib1 = 0
... fib2 = 1
... 
... # Print the first two numbers in the sequence
... print(fib1)
... print(fib2)
... 
... # Generate the next n-2 numbers in the sequence and print them
... for i in range(n-2):
...     fib3 = fib1 + fib2
...     print(fib3)
...     fib1 = fib2
...     fib2 = fib3
