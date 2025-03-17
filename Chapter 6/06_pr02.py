m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

overAllMarks = (m1 + m2 + m3)/3

if (overAllMarks >= 40):
    if (m1 >= 33 and m2 >= 33 and m3 >= 33):
        print("Pass")
    else:
        print("Fail due to one of the subject")
else:
    print("Fail due to overall percentage")