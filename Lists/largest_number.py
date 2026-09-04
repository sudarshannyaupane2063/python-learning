# To find largest number without using list functions 

num = [1,234,43,53,62,61,63,6,11,32,5]
largest = 0
for i in num:
    if i>largest:
        largest = i

print(largest,"is the largest number")