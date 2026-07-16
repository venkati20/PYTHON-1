
# Rent calculator.
# input of total rent .
# input of total food expense.
# input of electricity consumed.
# input of units consumed.
# pay of unit consumed

Rent= int(input("Total rent paid:"))
Food= int(input("Total food expense:"))
Electricity= int(input("Total elctricity units:"))
Units_consumed= int(input("Total units:"))
Persons= int(input("Total number of persons:"))
Pay_electricitybill=(Electricity*Units_consumed)

output=(Rent+Food+Pay_electricitybill)//Persons

print("total for each person:",output)