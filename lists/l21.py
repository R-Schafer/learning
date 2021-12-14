# making a new list without duplicating values

def new_list(original_list):
    updated_list= []
    for item in original_list:
        if item in original_list and item not in updated_list:
            updated_list.append(item)

    return updated_list


def main():
    original_list = ['Rainey', 'Charlie', 'Charlie', 'Honey', 'Rainey', 'Cow', 'Pig', 'Honey']
    print(new_list(original_list))  

main()