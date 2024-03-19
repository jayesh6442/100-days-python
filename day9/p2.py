student_score = {
    "jayesh": 78,
    "viral": 34,
    "savan": 56,
    "ayush": 34,
    "ansh": 56,
    "krutik": 34,
    "parth": 56,
}


student_makrs={}
for student in student_score:
    score = student_score[student]
    if score > 80:
        student_makrs[student]= "kya bat he"
    elif score > 70:
        student_makrs[student]= "vah bete wah"
    elif score > 40:
        student_makrs[student]= "padai kralo thoda"
    else:
        student_makrs[student]= "nikal lowde"
print(student_makrs)

for i in student_makrs:
    print(i , student_makrs[i])