# Lakeesha
# 06/27/2024
# P2HW2
# Calculating Grade Average
num1=(input("Enter grade for Module 1: "))
num2=(input("Enter grade for Module 2: "))
num3=(input("Enter grade for Module 3: "))
num4=(input("Enter grade for Module 4: "))
num5=(input("Enter grade for Module 5: "))
num6=(input("Enter grade for Module 6: "))
print()
print(" ------------Results------------")
# Python program to find smallest
# number in a list
 
# list of numbers
list1 = [num1,num2,num3,num4,num5,num6]
 
# sorting the list
list1.sort()
 
# printing the first element
print("Lowest Grade:", min(list1))
# Python program to find largest
# number in a list
 
# list of numbers
list1 = [65.5,88,78.5,90,61,92]
 
# sorting the list
list1.sort()
print(f"Higest Grade:", max(list1))
print("Sum of Grades:",sum(list1))





print(f"Average:} {sum(list1)/len(list1):.2f}")
print("---------------------------------------")



