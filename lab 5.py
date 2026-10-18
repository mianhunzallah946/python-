import numpy as np
marks=np.array([45,72,88,39,65,91,54,77,49,83])
arr_mean=sum(marks)/len(marks)
print(arr_mean)
print(max(marks))
print(min(marks))
sd=np.std(marks)
print(sd)
pmarks=marks[marks>=80]
print(pmarks)
amarks=marks[marks>=50]
print(amarks)

# count of pass marks
print(len(pmarks))
# count of all marks
print(len(amarks))

average=np.mean(marks)
print(average)
above_avg=marks[marks>average]
print(above_avg)

grace_marks=marks+5
print(grace_marks)

print(sum(pmarks))
    
    