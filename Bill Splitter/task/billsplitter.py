bills = {}

print('Enter the number of friends joining (including you):')
join_num = int(input())
if join_num <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(join_num):
        bills[input()] = 0
    print()
    print(bills)
