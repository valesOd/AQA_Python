def generateFibonacci(length):
   if length == 0:
      return [0]
   elif length == 1:
      return [0, 1]
   else:
      fib = generateFibonacci(length - 1)
      fib.append(fib[-1] + fib[-2])
      return fib
