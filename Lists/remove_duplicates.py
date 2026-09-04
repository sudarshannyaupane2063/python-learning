# To remove duplicates from given list 

num = [1,2,2,3,4,4,5]
unique = []
for i in num:
    if i not in unique:
        unique.append(i)

print(unique)