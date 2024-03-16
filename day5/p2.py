marks = input("Enter the marks: ").split()

for i in range(0,len(marks)):
    marks[i] = int(marks[i])
    
high_score=0
for score in marks:
    if score > high_score:
        high_score = score
print(high_score)
# print(max(marks))