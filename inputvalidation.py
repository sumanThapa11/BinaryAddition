#This function checks whether a number ranges from 0-255 or not.
def inputNumber(pos):
    valid = False
    while valid == False:
        try:
            num = int(input("Enter "+ pos +" number: "))    #taking input from user.
            while(num<0 or num>255):
                print("Please enter a number from 0 to 255 !!!")
                print()
                num = int(input("Enter a valid "+ pos +" number: "))
                print()
            valid = True
            return num
        except ValueError:
            print("Please enter a decimal number.")
            print()

#This function allows user to continue or terminate the program.
def wishToContinue(var):
    while var not in("y","n"):
        print("Please enter a valid value i.e.(y or n)!!!")
        print()
        var = input("Do you want to perform more calculation?(y/n)").lower() #storing a lowercase letter in var.
    return var



    
