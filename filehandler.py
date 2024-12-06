def calculate_weighted_grades(input_file, output_file):
    students = {}

    with open(input_file, 'r') as infile:
        for line in infile:
            name, unit, mark, weight = line.strip().split(', ')
            mark, weight = float(mark), float(weight)

            if name not in students:
                students[name] = 0
            students[name] += mark * (weight / 100)

    with open(output_file, 'w') as outfile:
        for name, final_mark in students.items():
            if final_mark >= 70:
                grade = "Distinction"
            elif final_mark >= 60:
                grade = "Merit"
            elif final_mark >= 50:
                grade = "Pass"
            else:
                grade = "Fail"
            
            outfile.write(f"{name.split()[0]}, {final_mark:.1f}, {grade}\n")

calculate_weighted_grades('input.txt', 'output.txt')
print("Grades calculated and written to output.txt.")
