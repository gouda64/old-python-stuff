import pygame

def translate():
  binary = input("Choose a binary number: ")
  decimal = 0
  for i in range(len(binary)):
    digit = int(binary[-1:]) # get the last digit
    decimal += 2 ** i * digit
    binary = binary[:-1] # remove the last digit
  return decimal


def main():
  final = translate()
  print("Binary: ", final)

if __name__ == "__main__":
  main()