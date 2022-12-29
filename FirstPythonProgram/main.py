import pandas as pd

print("Hello World")

name = input("What is your name? ")

print("Welcome " + name + " to repl.it!!")

for i in range(100):
  print(i)

n = 10
while n >= 1:
  print(n)
  n = n - 1

n = 0
while n <= 10:
  print(n)
  n = n + 1

number = input("Enter a number: ")
if (int(number) % 2 == 0):
  print("This number is even")
else:
  print("This number is odd")

def fib(n):
  a, b = 0, 1
  while a < n:
    print(a)
    a, b = b, a + b
fib(100)