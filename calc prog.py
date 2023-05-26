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