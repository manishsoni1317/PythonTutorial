try:
    print("Hello World")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a/b
    
except ValueError:
    print("Value Error, please fix it")
    
except ZeroDivisionError:
    c = "Infinite"
    
except Exception as e:
    print(f"This problem occurred {e}")
    print("Invalid input. Please enter a valid number.")

print("This is c: ", c)