 # Lakeesha King
 # 06/25/2024
 # Assignment Name
 # A brief description of the project


#lists
num_list= []
num1 = float(input("Enter a number:"))
num2 = float(input("enter a number:"))
num3 = float(input("enter a number:"))
num4 = float(input("enter a number:"))
num5 = float(input("enter a number:"))                   
num_list =[num1,num2,num3,num4,num5]
print(num_list)
lowest = min(num_list)
print (lowest)
highest = max(num_list)
print (highest)
total = sum(num_list)
print(total)
length=len(num_list)
average = total/length
print(average)
num_list.remove(lowest)
print(num_list)
