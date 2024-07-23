#python program for receipt Generator

from datetime import datetime
today=datetime.now()
quantity=int(input('Enter Total items:'))
bill={}
sum=0
for val in range (quantity):
    item = input('item :')
    price = eval(input('price :'))
    bill[item] = price
    sum += price
print('Dmart')
print('Date and Time:',today.strftime('%d/%m/%Y %H:%M:%S'))
print('*****************************************')
print('\n\nItem\tPrice')
for key in bill:
    print(key,'\t',bill[key])
print('\nTotal\t',sum)