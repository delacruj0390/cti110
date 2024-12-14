#Jesus Delacruz
#October 23, 2024
#P3HW2
#This program will calculater an employee salary and hours for regular pay and overtime hours and pay. 



# Enter the employee details
print("Enter the employee Details")

employees_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
rate_of_pay = float(input("Enter employee's pay rate: "))

# Calculate regular and overtime hours

overtime = max(0, hours_worked - 40)
regular = min(hours_worked, 40)

# Calculate pay

regular_pay = regular * rate_of_pay
overtime_pay = overtime * rate_of_pay * 1.5
gross_pay = regular_pay + overtime_pay

# Display the results

print("\nEmployee name:    ", employees_name)
print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-------------------------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f}{rate_of_pay:<12.2f}{overtime:<12.1f}${overtime_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<10.2f}")

