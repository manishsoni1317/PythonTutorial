def process(l, word):
    word = word.strip()
    if word in l:
        l.remove(word)
    return l

l1 = ['apple', 'banana', 'cherry', 'date']
l1 = process(l1, '   banana')
print(l1)