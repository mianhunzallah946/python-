temperatures=[28,31,35,29,37,33,26]
count=0
for temp in temperatures:
    if (temp>30):
        count=count+1
print(count)
avg=sum(temperatures)/len(temperatures)
print(avg)
print(max(temperatures))
print(min(temperatures))

# its done