def calculate_factorial(n):
    """Calculate the factorial of a number n."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    number = int(input("Enter a non-negative integer: "))
    
    if number < 0:
        print("Please enter a non-negative integer.")
        return
    
    for i in range(1, number + 1):
        print(f"{i}: {calculate_factorial(i)}")

if __name__ == "__main__":
    main()