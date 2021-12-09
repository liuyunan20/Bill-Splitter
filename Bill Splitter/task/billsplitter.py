bills = {}

print('Enter the number of friends joining (including you):')

try:
    join_num = int(input())
    assert join_num > 0
except ValueError:
    print('No one is joining for the party')
except AssertionError as err:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(join_num):
        bills[input()] = 0
    print()
    print('Enter the total bill value:')
    total_bill = int(input())
    for key in bills:
        bills[key] = round(total_bill / join_num, 2)
    print(bills)
