# Remove duplicates from a list.

def remove_duplicates(values):
    new_list = []
    for i in range(0, len(values)):
        if values[i] not in new_list:
            new_list.append(values[i])
                
    return new_list

def main():
    print(remove_duplicates([1, 2, 3, 1, 4, 4, 5]))

main()