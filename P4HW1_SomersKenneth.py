num_scores = int(input("Enter the number of scores: "))


scores = []


for i in range(num_scores):
    
    score = float(input("Enter score {}: ".format(i + 1)))
    
    
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        
        while True:
            score = float(input("Enter a valid score for score {}: ".format(i + 1)))
            if 0 <= score <= 100:
                break
    
    
    scores.append(score)


lowest_score = min(scores)

scores.remove(lowest_score)

average_score = sum(scores) / len(scores)


if 90 <= average_score <= 100:
    letter_grade = "A"
elif 80 <= average_score < 90:
    letter_grade = "B"
elif 70 <= average_score < 80:
    letter_grade = "C"
elif 60 <= average_score < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

print("-----------------------------Results---------------------------")
print("Lowest score: {}".format(lowest_score))
print("Score List after dropping lowest score: {}".format(scores))
print("Average score: {:.2f}".format(average_score))
print("Letter Grade: {}".format(letter_grade))

print("----------------------------------------------------------------")

