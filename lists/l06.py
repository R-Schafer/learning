# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Output: ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", ""]
i = 0
while i < len(list1):
    if list1[i] == "":
        list1.remove(list1[i])
    else:
        i = i + 1
print(list1)