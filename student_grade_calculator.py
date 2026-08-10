try:
    # 1. Take score input from the user
    score = float(input("Enter the student's score (0-100): "))

    # 2. Check if the score is within a valid range
    if 0 <= score <= 100:
        # 3. Determine the grade using conditional statements
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        # 4. Display the calculated grade
        print(f"The student's grade is: {grade}")
    else:
        print("Error: Score must be between 0 and 100.")

except ValueError:
    print("Invalid input! Please enter a numerical score.")
