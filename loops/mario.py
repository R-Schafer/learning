height= 4

for i in range(0, height):
    for j in range(height-i):
        print(" ", end="")
        
    for k in range(1 + i):
        print('#', end="")
        
    print(" ", end="")
    
    for m in range(1 + i):
        print("#", end="")
    
    print()

