oxford = {
    "gift": "Something willingly given to someone to show appreciation or love.",
    "this": "A keyword in c++",
    "youtube": "A video sharing platform",
    "instagram": "A photo sharing platform",
    "myList": [1, 3, 45]
}

print(oxford['this'])
# print(oxford['notpresent'])
print(oxford.get('notpresent'))

# oxford.update({"Manish": "Good Boy"}, myList=[1, 2, 3])

# oxford.update({"Manish": "Bad Boy"})

# print(oxford)
# print(oxford["this"])
# print(oxford.get("gift")

# print(oxford.items())

# for a, b in oxford.items():
#     print(a, "=:", b)

# for key in oxford.keys():
#     print(key, ":", oxford[key])