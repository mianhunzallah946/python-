# def status(mark):
#     if mark>=50:
#         print ('pass')
#     else:
#         print ('fail')
# status(45) 
def  percentage(obtained,total):
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
calc_percent=percentage(72,100)
print(calc_percent)
print(grade(calc_percent))