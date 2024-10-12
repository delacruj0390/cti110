
#Jesus Delacruz
#October 11,2024
#P2HW1_DelacruzJesus
#This program calculates travel expenses in a neater format





print('This program calculates and displays travel expenses')
print()
budget = float(input('Enter Budget:'))
print()
des = input('Enter your travel destination:')
print()
gas = float(input('How much do you think you will spend on gas?'))
print()
acc = float(input('Approximately, how much will you need for accomodation/hotel?'))
print()
food = float(input('Last, how much do you need for food?'))

#Total Values
exp = food + gas + acc
remain = budget - exp

#Results are organized in line
       
print()
print('\n----------Travel Expenses----------')
print(f'Location:            {des}')
print(f'Initial Budget:      ${budget:,.2f}')
print(f'Fuel:                ${gas:,.2f}')
print(f'Accomodation:        ${acc:,.2f}')
print(f'Food:                ${food:,.2f}')
print('---------------------------------------')
print()
print(f'Remaining Balance:   ${remain:,.2f}')
