# Delete set of keys from a dictionary
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# keysToRemove = ["name", "salary"]
# Output: {'age': 25, 'city': 'New york'}

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
remove = ["name", "salary"]

for key in remove:
    del sampleDict[key]
print(sampleDict)