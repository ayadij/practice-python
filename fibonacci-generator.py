def main():
  n = int(float(input("How many in your Fibonacci sequence? ")))
  print (fibonacci(n))
  
def fibonacci(n):
  if n <= 0: return []
  elif n == 1: return [1]
  else:
    fib = [1, 1]
    for x in range(2, n):
      fib.append(fib[x-2] + fib[x-1])
      print (fib)
    return fib
  
if __name__ == "__main__":
  main()