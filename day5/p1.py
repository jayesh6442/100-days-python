

height = input("Enter the height: ").split(" ")
for  i in range (0,len(height)):
    height[i]= int(height[i])
    
print(len(height))
    
avarage_height = int(sum(height)/len(height))

print(f"avarage  height is {avarage_height}")
