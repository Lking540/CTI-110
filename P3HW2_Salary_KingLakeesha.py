#Lakeesha King
#07/09/2024
#P3HW2 
#This program will calculate an empoyee's pay


name = input("enter the employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("enter employee's pay rate: "))

if hoursWorked > 40:
    # calculate overtime
    ovtHours = hoursWorked - 40
    # Calculate overtime pay
    ovtpay = ovtHours * (payRate * 1.5)
    # Calculate pay for regular hours
    regPay = 40 * payRate
    # calculate gross pay
    grossPay = regPay + ovtpay


else:
    # set over time hours and pay to zero
    ovtHours = 0
    ovtPay = 0
    regPay = payRate * hoursWorked
    grossPay = regPay 


print("-"*40)
print("Employee name: ",name,"\n")


print(f'{"hours Worked":<15}{"Pay Rate":<12}{"Over Time":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"gross Pay"}')
print("-" * 100)

print(f'{hoursWorked:<15}{payRate:<12}{ovtHours:<12}{ovtpay:<20.2f}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')


    
    
          
