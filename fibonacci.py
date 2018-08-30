def generateFibonacci(length):
   if length == 0:
      return 0
   elif length == 1:
      return 1
   else:                      
      return generateFibonacci(length-1) + generateFibonacci(length-2)


print(generateFibonacci(50))