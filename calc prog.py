def details ():
    Description = "Simple App Calculator using OOP concept."
    Date = "05-27-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

print("\nCalculator Program")
print("-------------------")

class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed!")
            return None

def main():
    calc = Calculator()

    while True:
        print("\nChoose a math operation:")
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("\nEnter your choice (1-4): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))