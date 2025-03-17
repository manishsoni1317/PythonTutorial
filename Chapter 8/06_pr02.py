def celtofar(cel):
    return cel * 9/5 + 32

def fartocel(far):
    return (far - 32) * 5/9

def main():
    print("Celsius to Fahrenheit")
    for i in range(0, 101, 10):
        print(i, "Celsius =", celtofar(i), "Fahrenheit")
    print("\nFahrenheit to Celsius")
    for i in range(0, 101, 10):
        print(i, "Fahrenheit =", fartocel(i), "Celsius")

main()