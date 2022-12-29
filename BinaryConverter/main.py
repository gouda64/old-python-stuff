import pygame

def translate():
  num = int(input("Chose a number: "))
  binary = ""
  while(num>0):
    binary = str(num % 2) + binary
    num = num // 2
  return binary

def main():
  binary_number = translate()
  print("Binary: " + binary_number)

if __name__ == "__main__":
  main()