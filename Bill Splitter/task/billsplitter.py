import random

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
    names = [input() for i in range(join_num)]
    bills = dict.fromkeys(names, 0)
    print()
    print('Enter the total bill value:')
    total_bill = int(input())
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_option = input()
    print()
    if lucky_option == 'Yes':
        lucky_one = random.choice(names)
        print(f'{lucky_one} is the lucky one!')
        for key in bills:
            bills[key] = round(total_bill / (join_num - 1), 2)
        bills[lucky_one] = 0
    else:
        print('No one is going to be lucky')
        for key in bills:
            bills[key] = round(total_bill / join_num, 2)
    print()
    print(bills)
