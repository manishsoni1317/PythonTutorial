oxford = {
    "lakdi": "Wood",
    "kursi": "Chair",
    "chaku": "Knife",
}
key = input("Enter the key: \n")
if(oxford.get(key) == None):
    print("The key is not present in the dictionary.")
else:
    print("The value is: ", oxford.get(key))