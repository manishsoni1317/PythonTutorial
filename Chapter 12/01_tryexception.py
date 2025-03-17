try:
    print("Hello World")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
    if b>=199:
        raise Exception("This number is too large")
    
except ValueError:
    print("Value Error, please fix it")
    
except ZeroDivisionError:
    print("This is a Zero division error block, please fix it")
    
except Exception as e:
    print(f"This problem occurred {e}")
    print("Invalid input. Please enter a valid number.")
    
else:
    print("Try was successful")
    
    
print("There were no errors")