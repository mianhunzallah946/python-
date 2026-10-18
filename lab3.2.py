def percentage(obtained,total):
    return (obtained/total)*100
def grade(mark):
    if mark>=90:
        return 'A'
    elif mark>=80:
        return 'B'
    elif mark>=70:
        return 'C'
    elif mark>=60:
        return 'D'
    elif mark>=50:
        return 'E'
    else:
        return 'F'
calc=percentage(42,100)

print(grade(percentage(53,100)))
print(grade(calc))