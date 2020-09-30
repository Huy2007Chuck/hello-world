# File: avg_score.py
# By: Huy2007Chuck

print("Enter your scores. Enter 0 when finished")
score = input()
total_score = 0
avg = 0
scores_entered = 0

while score != 0:
    scores_entered += 1
    total_score += int(score)
    avg = total_score / scores_entered

    print(avg)
    score = input()
