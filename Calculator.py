def calculate(num1, operator, num2):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        elif operator == '%':
            return num1 % num2
        elif operator == '**':
            return num1 ** num2
        elif operator == '//':
            return num1 // num2
        else:
            return "❌ Invalid operator!"
    except ZeroDivisionError:
        return "❌ Error: Division by zero!"

def display_operators():
    print("\nAvailable operations:")
    print("  +   Addition")
    print("  -   Subtraction")
    print("  *   Multiplication")
    print("  /   Division")
    print("  %   Modulus")
    print("  **  Exponentiation")
    print("  //  Floor Division")

def main():
    print("🧮 Welcome to the Python Calculator!")
    
    while True:
        display_operators()
        
        try:
            num1 = float(input("\nEnter the first number: "))
            operator = input("Choose an operator from above: ").strip()
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        result = calculate(num1, operator, num2)
        print(f"\n✅ Result: {num1} {operator} {num2} = {result}")

        again = input("\n🔁 Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("👋 Thanks for using the calculator!")
            break

if __name__ == "__main__":
    main()
