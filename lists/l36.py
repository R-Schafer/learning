# Print the numbers after removing even numbers from it. 

def odd_list(values):
    for i in values:
        if i % 2 == 0:
            values.remove(i)
      
    return values
    
def main():
    print(odd_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

main()