# remove items from list that are shorter in length than n

def find_len(names, n):
    i = 0
    while i < len(names):
        if len(names[i]) < n:
            names.remove(names[i])
        else:
            i += 1
    return names

def main():
    print(find_len(['Rainey', 'Honey', 'Charlie', 'Bill', 'Tom'], 5))

main()