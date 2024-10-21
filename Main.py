lucky_numbers = [4, 54, 15, 2, 60, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Toby"]

print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kelly"))

print(friends.count("Oscar"))

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.extend(lucky_numbers)
print(friends)

friends.clear()
print(friends)