string = input("Enter a string: ")
# Create an empty set to track characters we've already processed
processed = set()

for i in string:
    if i not in processed:
        freq = string.count(i)
        print(str(i) + ": " + str(freq), end=", ")
        processed.add(i)
