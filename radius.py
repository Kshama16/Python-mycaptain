Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> radius= float(input("1.1"))
1.1
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    radius= float(input("1.1"))
ValueError: could not convert string to float: ''
>>> area= math.pi * (radius  ** 1.1)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    area= math.pi * (radius  ** 1.1)
NameError: name 'math' is not defined
>>> print(" The area of the circle is:",3.8013271108436504)
 The area of the circle is: 3.8013271108436504
