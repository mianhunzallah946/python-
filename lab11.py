import pandas as pd
data={
    "Name":["ali","sara","usman","hina","bilal","noor"],
    "Hours":[2,5,1,6,3,7],
    "Attendace":[60,85,50,92,70,95],
    "Marks":[48,78,40,90,62,96]
}

fr=pd.DataFrame(data)
# fName=fr.Name[fr.Name>=80]
# fMarks=fr.Marks[fr.Marks>=80]
# print(fMarks)
std=fr[(fr['Hours']>=5) & (fr['Marks']>=70)]
print(std)

mstd=fr[(fr['Marks']<50) & (fr['Attendace']<60)]
print(mstd)