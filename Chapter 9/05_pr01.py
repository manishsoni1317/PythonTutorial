with open("poems.txt", "r") as f:
    if ('twinkle' in f.read()):
        print("Yes twinkle is present in the file.")
    else:
        print("No twinkle is not present in the file.")