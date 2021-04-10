# Calcox V1 is The Best Calculator Ever .. Coded by cLaS1c for his Python class  from Edugrade on April 2021
# In v2, we should catch errors, once the end user start to enter str for example, throw an error/usage message

User=input("What is your name ? ")
Usage="Hello, " + User + "Please choose a character from the following to do a specific operationn"
while True:
    OP=(input("Hello " + User + ", Please choose one of the following charachters (Case sensitive) 'X' for Multiplication, 'D' for Division," +
    "'A' for Addition, 'S' for Subtraction, 'P' for percentage and 'F' for factorial and 'E' to Exit the best program ever! :- "))
  ##  result=0
    if OP =="E":
         print("ByeBye!")
         exit()
    elif OP == "F":
            print("Kewl! will get the factorial for you")
            num = int(input("Please Enter a number"))
            fact = 1
            print ("Factorials of ", num , "are:- ")
            for i in range (1, num+1):
                fact= fact * i
                print( fact)    
            #print( str(FN) + " - " + str(SN)  + " = "  + str(FN - SN))    
    else:
        FN = int(input("Enter a first number :- "))
        SN = int(input("Enter a second  number :- "))
        if OP == "X":
            print("Kewl! Will do Multiplication for you")
            print( str(FN) + " * " + str(SN)  + " = "  + str(FN * SN))
        elif OP == "D":
            print("Kewl! Will do Division for you")
            print( str(FN) + " / " + str(SN)  + " = "  + str(FN / SN))
        elif OP == "A":
            print("Kewl! will do Addition for you")
            print( str(FN) + " + " + str(SN)  + " = "  + str(FN + SN))
        elif OP == "S":
            print("Kewl! will do subtracation for you")
            print( str(FN) + " - " + str(SN)  + " = "  + str(FN - SN))
        elif OP == "P":
            print("Kewl! will get the percentage for you")
            print( str(FN) + " % " + str(SN)  + " = "  + str(FN/100  * SN))
        else:
              print("Please read below, how to use the best calculator ;)  \n" +  Usage)
