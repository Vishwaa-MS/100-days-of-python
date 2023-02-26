#DAY-9
student_score={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

student_grade={}

for student in student_score:
    score =student_score[student]
    
    if score>90:
        student_grade[student]= "Outstandig"
    elif score>80:
        student_grade[student]= "Exceeds Expectations"
    elif score>70:
        student_grade[student]= "Acceptable"
    elif score<70:
        student_grade[student]="Try Harder"
    else:
        student_grade[student]="Try Again"
    
print(student_grade)
