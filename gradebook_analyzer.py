
# Title: Gradebook Analyzer
# Author: Himani Yadav
# Date: November 4, 2025

# Task 1: Welcome message and menu
def print_menu():
    print("\n=== Welcome to the Gradebook Analyzer ===")
    print("Choose an option:")
    print("1. Manual Data Entry")
    print("2. Exit\n")

# Task 2: Manual data entry
def manual_data_entry():
    marks = {}
    print("\nEnter student names and marks (type 'done' to finish):")
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        try:
            score = float(input(f"Enter marks for {name}: "))
            if score < 0 or score > 100:
                print("Marks must be between 0 and 100.")
                continue
            marks[name] = score
        except ValueError:
            print("Invalid input. Please enter a number.")
    return marks


# Task 3: Statistical analysis functions
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (scores[mid - 1] + scores[mid]) / 2
    else:
        return scores[mid]

def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else 0

def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else 0


# Task 4: Grade assignment and distribution
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
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
        grades[name] = grade
    return grades

def grade_distribution(grades_dict):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades_dict.values():
        if g in distribution:
            distribution[g] += 1
    return distribution

# Task 5: Pass/Fail filter using list comprehension
def pass_fail_lists(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]
    return passed_students, failed_students

# Task 6: Display results table
def display_results(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------")
    for name, score in marks_dict.items():
        print(f"{name:<12}\t{score:<6}\t{grades_dict[name]}")
    print("---------------------------------")

# Main program loop
def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            marks = manual_data_entry()
            if not marks:
                print("No data entered.")
                continue

            # Calculations
            avg = calculate_average(marks)
            med = calculate_median(marks)
            max_score = find_max_score(marks)
            min_score = find_min_score(marks)

            print("\n=== Statistical Summary ===")
            print(f"Average Score: {avg:.2f}")
            print(f"Median Score: {med:.2f}")
            print(f"Highest Score: {max_score}")
            print(f"Lowest Score: {min_score}")

            grades = assign_grades(marks)
            dist = grade_distribution(grades)

            print("\n=== Grade Distribution ===")
            for g, count in dist.items():
                print(f"{g}: {count} student(s)")

            passed, failed = pass_fail_lists(marks)
            print("\n=== Pass/Fail Summary ===")
            print(f"Passed ({len(passed)}): {', '.join(passed)}")
            print(f"Failed ({len(failed)}): {', '.join(failed)}")

            print("\n=== Detailed Results ===")
            display_results(marks, grades)

        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the program
if __name__ == "__main__":
    main()