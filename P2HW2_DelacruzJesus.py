
# Jesus Delacruz
# 13 October, 2024
# P2HW2
# This program has the user enter a grade, show results of grades by lowest, higest, sum of grades and average. 






# Ask user to enter the 6 grades

mod_1=float(input("Enter grade for module 1:  "))
mod_2=float(input("Enter grade for module 2:  "))
mod_3=float(input("Enter grade for module 3:  "))
mod_4=float(input("Enter grade for module 4:  "))
mod_5=float(input("Enter grade for module 5:  "))
mod_6=float(input("Enter grade for module 6:  "))


# Create a list to store grades

grades=[ ]

grades.append(mod_1)
grades.append(mod_2)
grades.append(mod_3)
grades.append(mod_4)
grades.append(mod_5)
grades.append(mod_6)


# Show results of grades

lowest_grades=min(grades)
highest_grades=max(grades)
sum_of_grades=sum(grades)
avg=sum_of_grades/6


# Show results of grades 

print("-----------Results-----------")

print("Lowest grade:    ",lowest_grades)

print("Highest grade:   ",highest_grades)

print("Sum of grades:   ",sum_of_grades)

print("Average:         ",avg)

print("----------------------------------------")



