#This function converts the decimal number to binary.
def decimalToBinary(num):
    
    bit = []    
    counter = 0
    while counter!=8:
        remainder = num % 2
        bit.append(remainder)
        num = num//2
        counter+=1

    return bit
