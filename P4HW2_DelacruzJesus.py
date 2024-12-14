# Jesus Delacruz

# 08 November, 2024

# P4HW2_DelacruzJesus

# The program will calculate gross pay for multiple employees, determined by user,
# and also calculates total amount paid for overtime,
# total amount paid for regular pay and total amount paid for all employees.

# Totals and counters
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0



# loop
while True:
    # Get employee name
    name = input("\nEnter employee's name or 'Done' to terminate: ")
    if name.lower() == "done":
        break

    # Employee details
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))

    # Calculate pay
    overtime_hours = max(0, hours_worked - 40)
    regular_hours = min(hours_worked, 40)
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    num_employees += 1

    # Display individual employee's pay
    print(f"\nEmployee name:    {name}")
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<14.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}${overtime_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<10.2f}")

# Display summary of all employees

print(f"Total number of employees entered: {num_employees}")

print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")

print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")

print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
