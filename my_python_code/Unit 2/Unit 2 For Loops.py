total = 0
total_scores = int(input("How many scores do you need? "))
for i in range(total_scores):
    score = int(input("Enter your score: "))
    total = total + score

average = total / total_scores
print(average)