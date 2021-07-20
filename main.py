import greetings
import inputvalidation
from decimaltobinary import decimalToBinary
import binaryaddition
import reverse_trim


greetings.greetingAtBeginning()

continuee = False
while continuee == False:

    firstNumber = inputvalidation.inputNumber("first")
    secondNumber = inputvalidation.inputNumber("second")

    revBinaryNumI = decimalToBinary(firstNumber)
    revBinaryNumII = decimalToBinary(secondNumber)

    binaryNumI = reverse_trim.reverse(revBinaryNumI)
    binaryNumII = reverse_trim.reverse(revBinaryNumII)

    binaryAddition = reverse_trim.reverse(binaryaddition.binaryAddition(binaryNumI,binaryNumII))

    finalOutput  =  reverse_trim.trim(binaryAddition)

    if len(finalOutput) <= 8:
        print("The binary addition of",firstNumber,"and",secondNumber,"results:",finalOutput)    #Displaying the sum.
        print("")

        var = input("Do you want to perform more calculation?(y/n)").lower()    #Asking user for continuation of program.
        if inputvalidation.wishToContinue(var) == "n":
            break
    else:
        print("The result of the addition exceeds 8-bits. Please enter other values!!")
    
    print("")
    print("*************************************************")
    print("")
    
greetings.greetingAtEnd()





