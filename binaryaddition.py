#This function returns sum and carry of two input bits.
def halfAdder(bit_a,bit_b):
    sum = bit_a ^ bit_b      #XOR gate producing sum of input bits.
    carry = bit_a and bit_b  #AND gate producing carry from input bits.

    return sum,carry

#This function carries out bit-wise binary addition. 
def fullAdder(bit_a,bit_b,carry):
    sum1,carry1 = halfAdder(bit_a,bit_b)
    sum2,carry2 = halfAdder(sum1,carry)

    return (sum2,carry1 or carry2)

#This function returns the sum of two binary numbers.
def binaryAddition(bits_a,bits_b):
    carry = 0
    result =[]

    for i in range(len(bits_a)-1,-1,-1):
        summ,carry = fullAdder(bits_a[i],bits_b[i],carry)
        result.append(summ)
    result.append(carry)
    return result
