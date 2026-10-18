import pandas as pd
data={
    "Name":["ali","sara","usman","hina","bilal","noor"],
    "Hours":[2,5,1,6,3,7],
    "Attendace":[60,85,50,92,70,95],
    "Marks":[48,78,40,90,62,96]
}
fr=pd.DataFrame(data)
print(fr.iloc[0]) #
print(fr.iloc[1:3])
print(fr.Marks[::-1])
print(fr.Marks[0::])    

print(fr.Attendace[::-1])
print(fr.loc[fr['Marks'].idxmax()])
