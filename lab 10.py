import pandas as pd
data={
    "Name":["ali","sara","usman","hina","bilal","noor"],
    "Hours":[2,5,1,6,3,7],
    "Attendace":[60,85,50,92,70,95],
    "Marks":[48,78,40,90,62,96]
}
fr=pd.DataFrame(data)
# print(fr)
cr=fr.shape
print(cr)

print(fr.Name)
# smarks=sum(fr.Marks)
# length=len(fr.Marks)

# avg=sum(smarks)/len
# print(avg)
average=fr['Marks'].mean()
print(average)

