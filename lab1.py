student="ali"
quiz=18
assignment=24
final=45
total_marks=quiz+assignment+final
print("Total Marks:", total_marks)

#percentage
percent=(total_marks/100)*100
print(percent)
if percent>=50:
    print("pass")
else:
    print("fail")