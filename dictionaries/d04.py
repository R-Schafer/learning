# Initialize dictionary with default values
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
# output: {"Kelly": {"designation": 'Application Developer', "salary": 8000}, 
#   "Emma": {"designation": 'Application Developer', "salary": 8000}, 
#   "John": {"designation": 'Application Developer', "salary": 8000}

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": "Application Developer", "salary": 8000}

newdict = {}

for employee in employees:
    newdict[employee] = {}

    # Copy defaults instead of sharing the same dictionary
    for key, value in defaults.items():
        newdict[employee][key] = value

newdict["Kelly"]["salary"] = 0
print(newdict)