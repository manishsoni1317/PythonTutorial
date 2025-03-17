def function():
    try:
        print("Hello World")
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a / b)

    except Exception as e:
        print(f"This problem occurred {e}")
        print("Invalid input. Please enter a valid number.")
        
    finally:
        print("Inside Finally")
    

# if __name__ == '__main__':
function()
print("main")