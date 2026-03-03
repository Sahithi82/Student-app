from student import Student

def process_students():
    with open("students.txt", "r") as file:
        lines = file.readlines()

    report_lines = []

    for line in lines:
        name, marks = line.strip().split(",")
        student = Student(name, marks)
        grade = student.calculate_grade()
        report_lines.append(f"{name} - {marks} - Grade: {grade}")

    with open("report.txt", "w") as report:
        for line in report_lines:
            report.write(line + "\n")

    print("Report generated successfully!")

if __name__ == "__main__":
    process_students()