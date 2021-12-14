# Remove empty strings from a list of strings

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Output: ['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "", None, "Eric", ""] 

i = 0
while i < len(str_list):
    if str_list[i] == "" or str_list[i] == None:
        str_list.remove(str_list[i])
    else:
        i += 1
        
print(str_list)