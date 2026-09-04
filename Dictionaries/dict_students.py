# To find highest & lowest scorer,above 80 scorers and calculates average in a dictionary 

students = {
    "Ram":78,
    "Sita":91,
    "Hari":65,
    "Shyam":41,
    "Gita":88,
    "Laxman":59
}
highest = 0
lowest = 0

#for highest scorer
for i in students:
    if students[i]>highest:
        highest = students[i]
for i in students:
    if students[i]==highest:
        print(i,"is the highest scorer.")

#for lowest scorer
lowest = highest
for i in students:
    if students[i]<lowest:
        lowest = students[i]
for i in students:
    if students[i]==lowest:
        print(i,"is the lowest scorer.")

#for average marks
print("Average marks of students is:",sum(students.values())/len(students))

#for above 80 scorers
print("Students who scored above 80 are:")
for i in students:
    if students[i]>80:
        print(i)