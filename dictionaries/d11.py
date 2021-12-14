# dictionary of birthdays

birthdays = {'Rainey': 'Feb 23', 'Charlie': 'Sept 16', 'Amber': 'Nov 1'}

while True:
    print('Enter a name: (blank to quit)\n')
    name = input().title()
    if name == '':
        break

    if name in birthdays:
        print(f'{name}s birthday is on {birthdays[name]}.')
    else:
        print(f'I do not have birthday information for {name}.')
        print('When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')