# list uniqueness checker
# if duplicates are found, the loop exits and prints duplicate found
items = ["apple", "banana", "orange", "apple", "mango"]
seen = set()
for item in items:
    if item in seen:
        print("duplicate found: ", item)
        break
    seen.add(item)
else:
    print("no duplicates found")