# Print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def colors(lst_colors):
    lst_colors.remove(lst_colors[5])
    lst_colors.remove(lst_colors[4])
    lst_colors.remove(lst_colors[0])
    return lst_colors

def main():
    print(colors(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
main()

