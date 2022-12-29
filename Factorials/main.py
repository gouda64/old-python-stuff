# compute the factorial
def factorial(n):
  if n == 1:
    return 1
  return(n * factorial(n - 1))

def main():
  #this program should compute the factorial of 5
  factorial_of_5 = factorial(5)
  #should print 120
  print(factorial_of_5)

if __name__ == "__main__":
  main()