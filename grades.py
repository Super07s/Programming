def main():
    mark = int(input("Enter the student's mark: "))

    if 70 <= mark <= 100:
        print("The grade is: A")
    elif 60 <= mark <= 69:
        print("The grade is: B")
    elif 50 <= mark <= 59:
        print("The grade is: C")
    elif 40 <= mark <= 49:
        print("The grade is: D")
    elif 30 <= mark <= 39:
        print("The grade is: E")
    elif 20 <= mark <= 29:
        print("The grade is: F")
    else:
        print("Invalid mark. Please enter a mark between 20 and 100.")

if __name__ == "__main__":
    main()
