# .join() & .split()


# .join()

', '.join(['cats', 'rats', 'bats'])
# 'cats, rats, bats'
' '.join(['My', 'name', 'is', 'Simon'])
# 'My name is Simon'
'ABC'.join(['My', 'name', 'is', 'Simon'])
# 'MyABCnameABCisABCSimon'

# .split()

'My name is Simon'.split()
# ['My', 'name', 'is', 'Simon']
'MyABCnameABCisABCSimon'.split('ABC')
# ['My', 'name', 'is', 'Simon']
'My name is Simon'.split('m')
# ['My na', 'e is Si', 'on']