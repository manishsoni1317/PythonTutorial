a = [1,2,3,4,5]
for i in a:
    print(i)
    if i == 3:
        break
        # continue
    print(i)
else:
    print("inside else")
print("finished")