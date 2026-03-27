n = int(input("Enter the Number of Students: "))

marks = []
for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    total += mark

average = total / n

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", average)
