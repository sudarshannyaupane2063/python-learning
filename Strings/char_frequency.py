# To find character frequency in a string

string = "banana"
frequency = {}
for i in string:
    if i not in frequency:
        frequency[i] = string.count(i)

print(frequency)