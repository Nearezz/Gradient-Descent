import math

palindromeArray = []
length = math.pow(10,3)


for i in range(1,int(length+1)):
    numDigit = str(i)
    firstDigit = int(numDigit[0])
    lengthOfDigit = len(numDigit)

    if (lengthOfDigit <= 3) and (i%10 == firstDigit): 
        palindromeArray.append(i)


    


print(palindromeArray)

