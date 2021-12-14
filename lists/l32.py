# Copy a list. 
import copy 

def make_copy(values):
    new_list = copy.copy(values)
    return new_list

def main():
    l1 = [1, 2, 3]
    l2 = make_copy(l1)
    l1.append(4)
    print(l1)
    print(l2)

main()