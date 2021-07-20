#This function returns reverse of the given list.  
def reverse(num):
    reverse = []
    for i in range(len(num)-1,-1,-1):
        reverse.append(num[i])

    return reverse

#This function removes unnecessary zero from the result.
def trim(result):
    finalString = ""
    i = 0

    try:
        
        while result[i] == 0:
            i += 1
        finalOutput = result[i:]    #Slicing the unnecessary zero.
    
    except IndexError:
        return "0"
    
      
    for j in range(0,len(finalOutput)):
        finalString = finalString + str(finalOutput[j])
    return finalString
    
