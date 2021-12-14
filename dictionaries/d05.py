# Create a new dictionary by extracting the following keys from a below dictionary
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# Output: {'name': 'Kelly', 'salary': 8000}

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys = ["name", "salary"]
newdict= {}

for x in keys:
    newdict[x] = sampleDict[x]

print(newdict)

