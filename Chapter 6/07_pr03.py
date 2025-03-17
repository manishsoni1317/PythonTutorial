spamWords = ["buy now", "subscribe this", "click here"]

# email = "this is a spam email. click here to buy now. subscribe this to get more spam emails."

email = input("Enter your email: ")
spam = False
if ("buy now" in email):
    spam = True
if ("subscribe this" in email):
    spam = True
if ("click here" in email):
    spam = True

print("spam is: ", spam)
    