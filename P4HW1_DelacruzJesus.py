# Jesus Delacruz

# 07 November, 2024

# P4HW1_DelacruzJesus

# Program will build on P2HW2 assignment. Instead of an individual statement to collect each score,
# the program will use a loop. Also, after displaying score average (after dropping lowest score)
# the program is to display a letter grade for the calculated average.


# Prompt user, how many scores they wish to enter?
num_scores = int(input("How many scores do you wish to enter? "))

# Create a empty list to store the scores
valid_scores = []

# Gather all scores in a loop
for i in range(num_scores):

    score = -1  # Initialize with an invalid score
    while score < 0 or score > 100: 
        score = float(input(f"Enter score #{i + 1}: "))
        if score < 0 or score > 100:

            print("Invalid Score!! Please enter a score between 0 and 100.")
    valid_scores.append(score)  

# Round out the lowest score and remove it
lowest_score = min(valid_scores)
valid_scores.remove(lowest_score)

# Calculate the average of the list
average_score = sum(valid_scores) / len(valid_scores)

# Determine a letter grade based on the average score
if average_score >= 90:
    letter_grade = 'A'

elif average_score >= 80:
    letter_grade = 'B'

elif average_score >= 70:
    letter_grade = 'C'

elif average_score >= 60:
    letter_grade = 'D'

else:
    letter_grade = 'F'

# Display all results

print("\n------------------Results------------------")

print(f"Lowest Score:        {lowest_score:.1f}")

print(f"Modified List:       {valid_scores}")

print(f"Scores Average:      {average_score:.2f}")

print(f"Grade:               {letter_grade}")

print("---------------------------------------------")
