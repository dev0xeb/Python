count = 0
score = int(input('Enter a score'))
total = 0

while score != -1:
    count+=1
    total += score
    score = int(input('Enter a score'))

average = total / count
print(average)
