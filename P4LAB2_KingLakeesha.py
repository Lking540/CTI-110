#Lakeesha King
#P4Lab2
#7/11/2024
# This program will display a multiplication table


#Use the while to control the program

keep_going = "yes"


while keep_going.lower() == "yes":
    #for loop goes here
    num = int(input("Enter an integer: "))
    print("\n")

    if num >=0:
        for i in range(1, 12 + 1):
            print(f'{num} * {i} = {num * i}')
        else:
            print("This program does not handle negative numbers")
            print("\n")

             

    keep_going = input("Would you like to run the program again? Enter yes or no: ")        



#input("Press enter key to exit")
print("The program has ended!")
   

