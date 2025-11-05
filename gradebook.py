# ------------------------------------------------------------
# Name: Varun
# Date: 05/11/2025
# Project: GradeBook Analyzer
# ------------------------------------------------------------
# Description:
# A simple Python program that helps analyze student marks.
# It supports manual entry or reading from a CSV file,
# calculates average, median, min, max, assigns grades,
# shows pass/fail lists, and exports results to a CSV file.
# ------------------------------------------------------------

import csv

# ---------- TASK 3: Statistical Functions ----------
def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    mid = n // 2
    if n % 2 != 0:
        return scores[mid]
    else:
        return (scores[mid - 1] + scores[mid]) / 2

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())

# ---------- TASK 4: Grade Assignment ----------
def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

# ---------- TASK 5: Pass / Fail Lists ----------
def pass_fail_lists(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    print("\nPass / Fail Summary:")
    print("--------------------")
    print(f"Passed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
    print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

# ---------- TASK 2: Data Entry or CSV Import ----------
def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks

def load_csv(filename):
    marks = {}
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) >= 2:
                    marks[row[0]] = float(row[1])
        print(f"\nLoaded {len(marks)} students from {filename}")
    except FileNotFoundError:
        print("Error: File not found. Please check the name and try again.")
    return marks

# ---------- TASK 6: Display Table ----------
def display_table(marks, grades):
    print("\nFinal Results Table")
    print("---------------------------")
    print("Name\t\tMarks\tGrade")
    print("---------------------------")
    for name in marks:
        print(f"{name:<12}\t{marks[name]:<7}\t{grades[name]}")
    print("---------------------------")

# ---------- BONUS: Export to CSV ----------
def export_to_csv(marks, grades, filename="final_results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])
        for name in marks:
            writer.writerow([name, marks[name], grades[name]])
    print(f"\nResults exported successfully to '{filename}'")

# ---------- TASK 1: Main Program ----------
def main():
    print("===================================")
    print("       GradeBook Analyzer")
    print("===================================\n")

    while True:
        print("Choose an option:")
        print("1. Manual data entry")
        print("2. Load data from CSV file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            marks = manual_input()
        elif choice == "2":
            filename = input("Enter CSV filename (e.g. marks.csv): ")
            marks = load_csv(filename)
            if not marks:
                continue
        elif choice == "3":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")
            continue

        # Perform analysis
        print("\n--- Statistical Analysis ---")
        print(f"Average Marks: {calculate_average(marks):.2f}")
        print(f"Median Marks : {calculate_median(marks):.2f}")
        print(f"Highest Score: {find_max_score(marks)}")
        print(f"Lowest Score : {find_min_score(marks)}")

        # Grade assignment
        grades = assign_grades(marks)

        # Grade distribution
        print("\nGrade Distribution:")
        print("-------------------")
        grade_count = {}
        for g in grades.values():
            grade_count[g] = grade_count.get(g, 0) + 1
        for g, c in grade_count.items():
            print(f"Grade {g}: {c} student(s)")

        # Pass / Fail summary
        pass_fail_lists(marks)

        # Display results table
        display_table(marks, grades)

        # Ask for export
        save = input("\nDo you want to save results to CSV file? (y/n): ")
        if save.lower() == "y":
            export_to_csv(marks, grades)

        again = input("\nDo you want to analyze another dataset? (y/n): ")
        if again.lower() != "y":
            print("Thank you for using GradeBook Analyzer!")
            break


# Run the program
if __name__ == "__main__":
    main()
