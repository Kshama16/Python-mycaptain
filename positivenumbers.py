Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> start= int(input("12"))
12
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    start= int(input("12"))
ValueError: invalid literal for int() with base 10: ''
>>> end = int(input("enter the end of the range:-14"))
enter the end of the range:-14
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    end = int(input("enter the end of the range:-14"))
ValueError: invalid literal for int() with base 10: ''
>>> print("12, -7, 5, 64, -14")
12, -7, 5, 64, -14
>>> for i in range(12,-14 +1)
SyntaxError: incomplete input
>>> if i>0:
