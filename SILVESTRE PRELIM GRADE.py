# Function to calculate preliminary grade
def calculate_prelim_grade(quiz_score, assignment_score, exam_score, participation_score):
    # Weights for each component (can be adjusted as needed)
    quiz_weight = 0.25
    assignment_weight = 0.30
    exam_weight = 0.35
    participation_weight = 0.10

    # Calculate prelim grade using weighted average
    prelim_grade = (quiz_score * quiz_weight) + (assignment_score * assignment_weight) + (exam_score * exam_weight) + (participation_score * participation_weight)
    return prelim_grade

# Main program
def main():
    print("Prelim Grade Calculator")
    
    # Input scores from the user
    quiz_score = float(input("Enter quiz average (0-100): "))
    assignment_score = float(input("Enter assignment average (0-100): "))
    exam_score = float(input("Enter exam score (0-100): "))
    participation_score = float(input("Enter participation score (0-100): "))
    
    # Calculate prelim grade
    prelim_grade = calculate_prelim_grade(quiz_score, assignment_score, exam_score, participation_score)
    
    # Output the calculated prelim grade
    print(f"Your preliminary grade is: {prelim_grade:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
    Your preliminary grade is: 88.15