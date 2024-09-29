#Jesus Delacruz
#September25,2024
#P1HW2_DelacruzJesus
#This program calculates travel expenses





print('This program calculates and displays travel expenses')
print()
budget = int(input('Enter Budget:'))
print()
des = input('Enter your travel destination:')
print()
gas = int(input('How much do you think you will spend on gas?'))
print()
acc = int(input('Approximately, how much will you need for accomodation/hotel?'))
print()
food = int(input('Last, how much do you need for food?'))

#Total Values
exp = food + gas + acc
remain = budget - exp

print()
print('----------Travel Expenses----------')
print('Location: ',des)
print('Initial Budget:',budget)
print()
print('Fuel:',gas)
print('Accomodation:',acc)
print('Food: ',food)
print()
print('Remaining Balance:',remain)
