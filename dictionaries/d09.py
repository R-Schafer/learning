# Get the key of a minimum value from the following dictionary
# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# Output: Math

sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
smallest = None

for key, value in sampleDict.items():
    if smallest == None:
        smallest = key
    elif value < sampleDict[smallest]:
        smallest = key

print(smallest)
