# Given two integer numbers, return the product. 
# If the product is greater than 1000, then return the sum

# just printing
input1 = int(input("Enter a number: \n"))
input2 = int(input("Enter a  2nd number: \n"))

x = input1 * input2
if x > 1000:
  y = input1 + input2
  print(y)
else:
  print(x)

# using a function
def numbers(input1, input2):
    x = input1 * input2
    if x > 1000:
      y = input1 + input2
      return y
    else:
      return x

input1 = int(input("Enter a number: \n"))
input2 = int(input("Enter a  2nd number: \n"))

print(numbers(input1, input2))


# testing a function
def numbers(input1, input2):
    x = input1 * input2
    if x > 1000:
      y = input1 + input2
      return y
    else:
      return x

input1 = int(input("Enter a number: \n"))
input2 = int(input("Enter a  2nd number: \n"))

def test_numbers():
  assert numbers(20, 30) == 600
  assert numbers(30, 40) == 70
  print("all works")

test_numbers() 

