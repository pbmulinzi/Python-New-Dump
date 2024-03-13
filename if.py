#Case of a buyer and conditions for down payment
print('''
Price of a house is $1,000,000.0

If buyer has good credit'
      they need to put down 10%
Otherwise
      they need to put down 20%
Print the down payment
''')
is_GoodCredit = True
is_NotGoodCredit = False

if is_GoodCredit:
    put_down =(0.1*1000000)
    next = f'They need to put down ${put_down}'
    print(next)
else:
    put_down =(0.2*1000000)
    next = f'They need to put down ${put_down}'
    print(next)
    
